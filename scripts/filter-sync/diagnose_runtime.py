#!/usr/bin/env python3
"""Read-only metadata report for the existing BadkamerCity search runtime.

Run in an already authorized VPS shell: sudo python3 - < diagnose_runtime.py
No index/file writes, package installation, restarts or credential output.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener


CONTAINER = "badkamercity-filter-api-verified-candidate"
TYPESENSE = "http://127.0.0.1:8108"
REQUIRED_ENV = ("SHOPIFY_ADMIN_ACCESS_TOKEN", "SHOPIFY_CLIENT_ID",
                "SHOPIFY_CLIENT_SECRET", "TYPESENSE_API_KEY")
ENV_NAME = re.compile(r"^[A-Z][A-Z0-9_]{0,95}$")
IDENTIFIER = re.compile(r"^[A-Za-z0-9_.-]{1,160}$")
SCRIPT_PATH = re.compile(r"/[A-Za-z0-9_./@+\-]+\.(?:py|sh|mjs|cjs|js|ps1)\b")
JOB_NAME = re.compile(r"\b[A-Za-z0-9_.@:\-]+\.(?:timer|service)\b")
RELATED = re.compile(r"badkamer|typesense|shopify|(?:^|[/_.-])bc[_-]|index|sync", re.I)
SKIP_DIRS = {".git", ".cache", "node_modules", "venv", ".venv", "__pycache__",
             "site-packages", "images", "media", "logs", "exports", "raw"}


def credential_name(name):
    return bool(ENV_NAME.fullmatch(name) and
                (name in REQUIRED_ENV or re.search(r"(?:KEY|TOKEN|SECRET|PASSWORD|CLIENT_ID)$", name)))


class Redactor:
    def __init__(self):
        self.values = set()

    def register(self, env):
        for name, value in env.items():
            if credential_name(name) and isinstance(value, str) and len(value.strip()) >= 4:
                self.values.add(value.strip().strip("\"'"))

    def clean(self, value):
        if isinstance(value, dict):
            return {self.clean(str(k)): self.clean(v) for k, v in value.items()}
        if isinstance(value, list):
            return [self.clean(v) for v in value]
        if isinstance(value, str):
            for secret in sorted(self.values, key=len, reverse=True):
                if secret:
                    value = value.replace(secret, "[REDACTED]")
            return value
        return value


def env_metadata(env, redactor):
    redactor.register(env)
    names = sorted(set(REQUIRED_ENV) | {n for n in env if credential_name(n)})
    return [{"name": name, "present": name in env,
             "nonempty": bool(str(env.get(name, "")).strip())} for name in names]


def safe_text(value, limit=500):
    if not isinstance(value, str) or len(value) > limit or any(ord(c) < 32 for c in value):
        return "[INVALID_METADATA]"
    return value


def command_allowed(argv):
    if argv == ["docker", "inspect", CONTAINER]:
        return True
    if argv == ["systemctl", "list-timers", "--all", "--no-pager", "--no-legend"]:
        return True
    if (len(argv) == 5 and argv[:2] == ["crontab", "-u"] and
            argv[2] in {"root", "ubuntu"} and argv[3:] == ["-l", "--"]):
        return True
    if (len(argv) == 4 and argv[:2] == ["crontab", "-u"] and
            argv[2] in {"root", "ubuntu"} and argv[3] == "-l"):
        return True
    if len(argv) == 4 and argv[:2] == ["systemctl", "show"]:
        return bool(JOB_NAME.fullmatch(argv[2]) and argv[3] ==
                    "--property=FragmentPath,ActiveState,UnitFileState,Triggers,EnvironmentFiles,ExecStart")
    return False


def run_command(argv):
    if not command_allowed(argv):
        return {"status": "COMMAND_REFUSED", "stdout": ""}
    try:
        result = subprocess.run(argv, capture_output=True, text=True, timeout=10, check=False)
        if result.returncode:
            return {"status": "COMMAND_FAILED", "stdout": ""}
        if len(result.stdout) > 1_000_000:
            return {"status": "OUTPUT_LIMIT", "stdout": ""}
        return {"status": "OK", "stdout": result.stdout}
    except subprocess.TimeoutExpired:
        return {"status": "COMMAND_TIMEOUT", "stdout": ""}
    except OSError:
        return {"status": "COMMAND_UNAVAILABLE", "stdout": ""}


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise URLError("redirect refused")


def local_json(path, key, opener=None):
    url = TYPESENSE + path
    parsed = urlsplit(url)
    route = path.split("?", 1)[0]
    allowed_route = route == "/aliases" or bool(re.fullmatch(
        r"/collections/[A-Za-z0-9_.-]{1,160}(?:/documents/search)?", route))
    if (parsed.scheme != "http" or parsed.hostname != "127.0.0.1" or parsed.port != 8108
            or not allowed_route or ".." in path):
        return None, "URL_REFUSED"
    request = Request(url, method="GET", headers={"X-TYPESENSE-API-KEY": key})
    open_request = opener or build_opener(ProxyHandler({}), NoRedirect()).open
    try:
        with open_request(request, timeout=10) as response:
            raw = response.read(2_000_001)
        if len(raw) > 2_000_000:
            return None, "RESPONSE_LIMIT"
        return json.loads(raw), "OK"
    except HTTPError as error:
        return None, "HTTP_" + str(error.code)
    except (URLError, TimeoutError, OSError):
        return None, "CONNECTION_FAILED"
    except (ValueError, UnicodeError):
        return None, "INVALID_JSON"


def id_format(value):
    if isinstance(value, str):
        if re.fullmatch(r"gid://shopify/[A-Za-z]+/[0-9]+", value):
            return "shopify_gid"
        if value.isdecimal():
            return "numeric_string"
        return "other_string"
    if type(value) is int:
        return "integer"
    return "missing" if value is None else type(value).__name__


def typesense_report(env, redactor, opener=None):
    collection = env.get("TYPESENSE_COLLECTION", "")
    if not IDENTIFIER.fullmatch(collection):
        return {"status": "NO_VALID_COLLECTION_NAME"}
    keys = [name for name in env if name.startswith("TYPESENSE") and
            credential_name(name) and env[name]]
    key_name = "TYPESENSE_API_KEY" if env.get("TYPESENSE_API_KEY") else (keys[0] if len(keys) == 1 else None)
    if not key_name:
        return {"status": "NO_UNAMBIGUOUS_EXISTING_KEY", "collection": collection}
    redactor.register(env)
    key = env[key_name]
    schema, status = local_json("/collections/" + quote(collection, safe=""), key, opener)
    report = {"status": status, "collection": collection, "credential_name": key_name}
    if status != "OK" or not isinstance(schema, dict):
        return report
    report["document_count"] = schema.get("num_documents") if type(schema.get("num_documents")) is int else None
    report["schema_name"] = safe_text(schema.get("name", ""), 160)
    report["schema_fields"] = [{"name": safe_text(x.get("name", ""), 160),
                                "type": safe_text(x.get("type", ""), 40),
                                "facet": bool(x.get("facet", False)),
                                "optional": bool(x.get("optional", False))}
                               for x in schema.get("fields", [])[:400] if isinstance(x, dict)]
    report["schema_fields_truncated"] = len(schema.get("fields", [])) > 400
    aliases, alias_status = local_json("/aliases", key, opener)
    report["aliases_status"] = alias_status
    report["aliases"] = [{"name": x["name"], "collection_name": x["collection_name"]}
                         for x in (aliases or {}).get("aliases", [])[:100]
                         if isinstance(x, dict) and IDENTIFIER.fullmatch(x.get("name", ""))
                         and IDENTIFIER.fullmatch(x.get("collection_name", ""))] if isinstance(aliases, dict) else []
    query = urlencode({"q": "*", "query_by": "title", "per_page": 1,
                       "include_fields": "id,shopify_product_id,collection_ids"})
    sample, sample_status = local_json("/collections/" + quote(collection, safe="") +
                                       "/documents/search?" + query, key, opener)
    report["sample_status"] = sample_status
    hits = sample.get("hits", []) if isinstance(sample, dict) else []
    if hits and isinstance(hits[0], dict) and isinstance(hits[0].get("document"), dict):
        doc = hits[0]["document"]
        # Report formats, never actual document values, titles or customer fields.
        report["sample_identity_formats"] = {
            "field_names": sorted(k for k in doc if k in {"id", "shopify_product_id", "collection_ids"}),
            "id": id_format(doc.get("id")),
            "shopify_product_id": id_format(doc.get("shopify_product_id")),
            "collection_ids": sorted({id_format(x) for x in doc.get("collection_ids", [])})
                if isinstance(doc.get("collection_ids"), list) else id_format(doc.get("collection_ids"))}
    return report


def parse_env(text):
    env = {}
    for line in text.splitlines():
        match = re.match(r"\s*(?:export\s+)?([A-Z][A-Z0-9_]*)\s*=\s*(.*)$", line)
        if match and credential_name(match[1]):
            env[match[1]] = match[2].strip().strip("\"'")
    return env


def discover_roots(home=Path("/home/ubuntu"), opt=Path("/opt/badkamercity"), mounts=()):
    roots = [opt]
    try:
        roots.extend(x for x in sorted(home.glob("bc*")) if x.is_dir() and not x.is_symlink())
    except OSError:
        pass
    for mount in mounts:
        path = Path(mount)
        if path == opt or str(path).startswith(str(home) + "/bc"):
            roots.append(path)
    roots = list(dict.fromkeys(x for x in roots if x.is_dir() and not x.is_symlink()))
    # Recent sync deployments come before old trial folders in the bounded scan.
    def priority(path):
        try:
            modified = path.stat().st_mtime
        except OSError:
            modified = 0
        return ("sync" not in path.name.casefold(), -modified, str(path))
    selected = sorted(roots, key=priority)[:50]
    if opt in roots and opt not in selected:
        selected[-1:] = [opt]
    return selected


def scan_runtime_files(roots, redactor):
    scripts, env_files, seen, examined, bytes_read, limits = [], [], set(), 0, 0, []
    signals = ("index", "sync", "shopify", "typesense", "webhook", "updated_at")
    for root in roots:
        try:
            candidates = sorted(root.glob(".env*"))
        except OSError:
            candidates = []
        for path in candidates:
            try:
                if path.is_file() and not path.is_symlink() and path.stat().st_size <= 200_000:
                    env_files.append({"path": str(path), "credentials":
                                      env_metadata(parse_env(path.read_text(errors="replace")), redactor)})
            except OSError:
                pass
        for directory, subdirs, names in os.walk(root, followlinks=False):
            here = Path(directory)
            depth = len(here.relative_to(root).parts)
            subdirs[:] = sorted(x for x in subdirs if x not in SKIP_DIRS and not x.startswith(".")
                                and not (here / x).is_symlink()) if depth < 4 else []
            for name in sorted(names):
                path = here / name
                if str(path) in seen or path.is_symlink() or path.suffix not in {".py", ".sh", ".ps1", ".js", ".mjs", ".cjs", ".service", ".timer"}:
                    continue
                seen.add(str(path)); examined += 1
                if examined > 1500 or bytes_read > 20_000_000 or len(scripts) >= 100:
                    limits.append("SCRIPT_SCAN_LIMIT")
                    return {"roots": [str(x) for x in roots], "scripts": scripts,
                            "env_files": env_files, "limits": sorted(set(limits))}
                try:
                    stat = path.stat()
                    if stat.st_size > 1_000_000:
                        continue
                    raw = path.read_bytes(); bytes_read += len(raw)
                    text = raw.decode("utf-8", errors="replace")
                except OSError:
                    continue
                found = [signal for signal in signals if signal in text.casefold() or signal in name.casefold()]
                if found:
                    scripts.append({"path": str(path), "size_bytes": stat.st_size,
                                    "modified_at": dt.datetime.fromtimestamp(stat.st_mtime, dt.timezone.utc).isoformat(),
                                    "sha256": hashlib.sha256(raw).hexdigest(), "signals": found,
                                    "credential_names_referenced": sorted({x for x in re.findall(r"\b(?:SHOPIFY|TYPESENSE)_[A-Z0-9_]+\b", text) if credential_name(x)})})
    return {"roots": [str(x) for x in roots], "scripts": scripts,
            "env_files": env_files, "limits": sorted(set(limits))}


def job_metadata(text, source, redactor):
    redactor.register(parse_env(text))
    jobs = []
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"\s*(?:export\s+)?[A-Z][A-Z0-9_]*\s*=", line):
            continue
        if not RELATED.search(line):
            continue
        jobs.append({"source": safe_text(source), "script_paths": sorted(set(SCRIPT_PATH.findall(line)))[:20],
                     "uses_docker": "docker" in line, "uses_python_module": bool(re.search(r"python[0-9.]*\s+-m\s+", line))})
    return jobs[:50]


def jobs_report(runner, redactor, cron_root=Path("/etc")):
    timer_result = runner(["systemctl", "list-timers", "--all", "--no-pager", "--no-legend"])
    names = sorted({x for x in JOB_NAME.findall(timer_result.get("stdout", "")) if RELATED.search(x)})[:30]
    timers, cron = [], []
    for name in names:
        result = runner(["systemctl", "show", name,
                         "--property=FragmentPath,ActiveState,UnitFileState,Triggers,EnvironmentFiles,ExecStart"])
        props = dict(line.split("=", 1) for line in result.get("stdout", "").splitlines() if "=" in line)
        timers.append({"name": name, "status": result["status"],
                       "active_state": props.get("ActiveState") if props.get("ActiveState") in {"active", "inactive", "failed", "activating", "deactivating"} else None,
                       "unit_file_state": props.get("UnitFileState") if props.get("UnitFileState") in {"enabled", "disabled", "static", "masked", "generated", "enabled-runtime"} else None,
                       "fragment_path": safe_text(props.get("FragmentPath", "")),
                       "script_paths": sorted(set(SCRIPT_PATH.findall(props.get("ExecStart", ""))))[:20],
                       "triggers": sorted(set(JOB_NAME.findall(props.get("Triggers", ""))))[:10],
                       "environment_file_paths": sorted(set(re.findall(r"/[A-Za-z0-9_./@+\-]+", props.get("EnvironmentFiles", ""))))[:10]})
    statuses = {}
    for user in ("root", "ubuntu"):
        result = runner(["crontab", "-u", user, "-l"])
        statuses[user] = result["status"]
        cron.extend(job_metadata(result.get("stdout", ""), "crontab:" + user, redactor))
    files = [cron_root / "crontab"]
    try:
        files.extend(sorted((cron_root / "cron.d").iterdir())[:50])
    except OSError:
        pass
    for path in files:
        try:
            if path.is_file() and not path.is_symlink() and path.stat().st_size <= 100_000:
                cron.extend(job_metadata(path.read_text(errors="replace"), str(path), redactor))
        except OSError:
            pass
    return {"timer_listing_status": timer_result["status"], "units": timers,
            "crontab_status": statuses, "cron_jobs": cron[:100]}


def build_report(runner=run_command, environ=None, opener=None,
                 home=Path("/home/ubuntu"), opt=Path("/opt/badkamercity"), cron_root=Path("/etc")):
    redactor = Redactor()
    report = {"schema_version": 1, "read_only": True, "writes_performed": False,
              "effective_uid": os.geteuid(), "process_credentials": env_metadata(dict(os.environ if environ is None else environ), redactor)}
    result = runner(["docker", "inspect", CONTAINER])
    docker = {"name": CONTAINER, "inspection_status": result["status"]}
    roots, env, mounts = [], {}, []
    if result["status"] == "OK":
        try:
            items = json.loads(result["stdout"])
            item = items[0] if isinstance(items, list) and len(items) == 1 else {}
            env = dict(x.split("=", 1) for x in item.get("Config", {}).get("Env", []) if isinstance(x, str) and "=" in x)
            docker.update({"running": item.get("State", {}).get("Running") is True,
                           "image_ref": safe_text(item.get("Config", {}).get("Image", "")),
                           "image_id": safe_text(item.get("Image", "")),
                           "credentials": env_metadata(env, redactor)})
            docker["mounts"] = [{"type": safe_text(x.get("Type", ""), 30),
                                  "source": safe_text(x.get("Source", "")),
                                  "destination": safe_text(x.get("Destination", "")),
                                  "read_only": x.get("RW") is False} for x in item.get("Mounts", [])[:30] if isinstance(x, dict)]
            mounts = [x["source"] for x in docker["mounts"]]
            report["typesense"] = typesense_report(env, redactor, opener)
        except (ValueError, TypeError, KeyError, IndexError):
            docker["inspection_status"] = "INVALID_INSPECT_RESPONSE"
    report["docker"] = docker
    roots = discover_roots(home, opt, mounts)
    report["runtime_files"] = scan_runtime_files(roots, redactor)
    report["jobs"] = jobs_report(runner, redactor, cron_root)
    report["limitations"] = ["Metadata only: no script bodies, environment values or raw commands.",
                              "Named container and bounded bc* directories only; absence outside this scope is not established.",
                              "No Shopify capture, synchronization, index mutation, restart or deployment performed."]
    return redactor.clean(report)


def main():
    try:
        report = build_report()
    except Exception:
        # Exception bodies can contain commands or private configuration.
        report = {"schema_version": 1, "read_only": True, "writes_performed": False,
                  "status": "DIAGNOSTIC_FAILED_DETAILS_SUPPRESSED"}
    print(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
