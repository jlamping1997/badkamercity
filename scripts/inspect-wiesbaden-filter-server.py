"""Read-only diagnosis for SKU 24.3710 on the existing filter VPS.

Run after normal SSH login, with sudo if Docker requires it. Prints only a
sanitized JSON report. No product/index/config writes, imports or restarts.
Never print docker inspect output, environment values, keys or raw exceptions.
"""
import ast
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.error
import urllib.parse
import urllib.request

PRODUCT_ID = "10657256210698"
SKU = "24.3710"
CONTAINERS = [
    "badkamercity-filter-api-verified-candidate",
    "badkamercity-filter-api-v3",
]
CODE_ROOTS = [
    Path("/opt/badkamercity"),
    Path("/home/ubuntu/bc_apiproef_20261013"),
    Path("/home/ubuntu/bc_filterindex_20261013_874e415c15"),
]
SAFE_STRINGS = {
    "", " ", "\n", "\r\n", ",", ":", "utf-8", "utf8",
    "sku", "values", "fields", "version", "format",
    "values_sha256", "filter_manifest",
}


class RedactLiterals(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, str) and node.value not in SAFE_STRINGS:
            return ast.copy_location(ast.Constant(value="[REDACTED_LITERAL]"), node)
        return node


def safe_hash_code(text):
    """Expose calculation syntax, replacing arbitrary string/bytes literals."""
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError):
        return []
    result = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Assign, ast.Return)):
            continue
        source = ast.get_source_segment(text, node) or ""
        if not any(term in source for term in ("values_sha256", "filter_manifest", "hashlib.sha256")):
            continue
        if len(source) > 20000:
            continue
        # Bytes may contain credentials too; do not include such statements.
        if any(isinstance(n, ast.Constant) and isinstance(n.value, bytes) for n in ast.walk(node)):
            continue
        sanitized = RedactLiterals().visit(copy.deepcopy(node))
        result.append({"line": node.lineno, "code": ast.unparse(ast.fix_missing_locations(sanitized))})
        if len(result) >= 12:
            break
    return result


def inspect_container(name):
    try:
        proc = subprocess.run(
            ["docker", "inspect", name], capture_output=True, text=True, timeout=15
        )
    except (OSError, subprocess.TimeoutExpired):
        return None, "DOCKER_UNAVAILABLE_OR_TIMEOUT"
    if proc.returncode:
        # stderr can contain environment details; only classify it in memory.
        error = proc.stderr.lower()
        if "permission denied" in error:
            return None, "DOCKER_PERMISSION_DENIED"
        if "no such" in error:
            return None, "CONTAINER_NOT_FOUND"
        return None, "DOCKER_INSPECT_FAILED"
    try:
        items = json.loads(proc.stdout)
        return items[0] if len(items) == 1 else None, "OK"
    except (ValueError, IndexError):
        return None, "INVALID_INSPECT_RESPONSE"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise RuntimeError("REDIRECT_REFUSED")


def read_index_document(container):
    env = dict(
        item.split("=", 1)
        for item in container.get("Config", {}).get("Env", [])
        if "=" in item
    )
    collection = env.get("TYPESENSE_COLLECTION")
    keynames = [
        name for name in env
        if name.upper().startswith("TYPESENSE")
        and ("KEY" in name.upper() or "TOKEN" in name.upper())
    ]
    if not collection or len(keynames) != 1:
        return {"status": "NO_UNAMBIGUOUS_EXISTING_CONFIGURATION"}
    # Match the existing typesense_support.py workflow: only loopback, GET.
    url = (
        "http://127.0.0.1:8108/collections/"
        + urllib.parse.quote(collection, safe="")
        + "/documents/" + PRODUCT_ID
    )
    request = urllib.request.Request(
        url, method="GET", headers={"X-TYPESENSE-API-KEY": env[keynames[0]]}
    )
    try:
        with urllib.request.build_opener(NoRedirect()).open(request, timeout=15) as response:
            doc = json.load(response)
        if doc.get("sku") != SKU or doc.get("id") != PRODUCT_ID:
            return {"status": "PRODUCT_ID_OR_SKU_MISMATCH"}
        allowed = [
            "id", "sku", "f_aantal_kraangaten", "source_updated_at",
            "collection_handles", "f_serie", "f_materiaal", "f_kraanmontage",
        ]
        return {"status": "OK", "collection": collection,
                "document": {key: doc[key] for key in allowed if key in doc}}
    except urllib.error.HTTPError as exc:
        return {"status": "TYPESENSE_HTTP_" + str(exc.code)}
    except Exception:
        return {"status": "TYPESENSE_READ_FAILED_NO_DETAILS_LOGGED"}


def collect_code(roots):
    records, seen = [], set()
    for root in roots:
        if not root.is_dir() or root.is_symlink():
            continue
        for directory, subdirs, names in os.walk(root, followlinks=False):
            subdirs[:] = [
                name for name in subdirs
                if not name.startswith(".")
                and name not in ("node_modules", "venv", "__pycache__", "site-packages")
                and not (Path(directory) / name).is_symlink()
            ]
            for name in names:
                path = Path(directory) / name
                if path.suffix not in (".py", ".js", ".cjs", ".mjs", ".sh", ".ps1"):
                    continue
                if path.is_symlink() or str(path) in seen:
                    continue
                seen.add(str(path))
                try:
                    if path.stat().st_size > 2_000_000:
                        continue
                    data = path.read_bytes()
                    text = data.decode("utf-8")
                except (OSError, UnicodeError):
                    continue
                terms = [
                    term for term in ("values_sha256", "filter_manifest", "documents/import",
                                      "documents/", "hashlib.sha256")
                    if term in text
                ]
                if terms:
                    records.append({
                        "path": str(path), "sha256": hashlib.sha256(data).hexdigest(),
                        "terms": terms,
                        "calculation_sanitized": safe_hash_code(text) if path.suffix == ".py" else [],
                    })
                if len(seen) >= 4000:
                    return records, "LIMIT_4000_CODE_FILES"
    return records, "COMPLETE_WITHIN_NAMED_ROOTS"


def main():
    report = {"sku": SKU, "read_only": True, "effective_uid": os.geteuid(),
              "containers": [], "writes_performed": False}
    roots = list(CODE_ROOTS)
    for name in CONTAINERS:
        container, status = inspect_container(name)
        record = {"name": name, "inspection": status}
        if container:
            record["running"] = bool(container.get("State", {}).get("Running"))
            record["code_mounts"] = [
                {"source": mount["Source"], "destination": mount["Destination"]}
                for mount in container.get("Mounts", [])
                if mount.get("Type") == "bind"
                and mount.get("Destination") == "/opt/bc_candidate"
            ]
            roots.extend(Path(mount["source"]) for mount in record["code_mounts"])
            if name == CONTAINERS[0]:
                record["target_document"] = read_index_document(container)
        report["containers"].append(record)
    report["code"], report["code_scan"] = collect_code(roots)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
