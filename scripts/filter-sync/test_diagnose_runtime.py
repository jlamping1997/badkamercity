"""Offline tests; no Docker, SSH, live HTTP or production filesystem access."""
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError


spec = importlib.util.spec_from_file_location("diagnose", Path(__file__).with_name("diagnose_runtime.py"))
diagnose = importlib.util.module_from_spec(spec)
spec.loader.exec_module(diagnose)


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class RuntimeDiagnosticTests(unittest.TestCase):
    def test_report_is_useful_and_never_exposes_credentials_or_document_values(self):
        secrets = ["TS_PRIVATE_TOKEN_ABCDEFGHI", "SHOPIFY_PRIVATE_SECRET_ABCDEFGHI",
                   "ENVFILE_PRIVATE_TOKEN_ABCDEFGHI", "PROCESS_PRIVATE_TOKEN_ABCDEFGHI"]
        commands, requests = [], []
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            home = root / "home"; home.mkdir()
            sync = home / "bc_sync_20261103"; sync.mkdir()
            opt = root / "opt"; opt.mkdir()
            (sync / "sync_catalog.py").write_text("import os\n# SHOPIFY_CLIENT_SECRET sync Typesense\nTOKEN='DO_NOT_PRINT_SOURCE_LITERAL'\n")
            (sync / ".env").write_text("SHOPIFY_ADMIN_ACCESS_TOKEN=" + secrets[2] + "\n")
            etc = root / "etc"; (etc / "cron.d").mkdir(parents=True)
            (etc / "cron.d" / "bc-index").write_text("*/5 * * * * ubuntu python3 /home/ubuntu/bc_sync_20261103/sync_catalog.py --token DO_NOT_PRINT_CRON_ARGUMENT\n")
            inspect = [{"State": {"Running": True}, "Image": "sha256:1234",
                        "Config": {"Image": "bc-filter-api:current", "Env": [
                            "TYPESENSE_COLLECTION=bc_sync_20261103t120045_4e7799",
                            "TYPESENSE_API_KEY=" + secrets[0],
                            "SHOPIFY_CLIENT_SECRET=" + secrets[1]],
                            "Cmd": ["--password", "DO_NOT_PRINT_DOCKER_COMMAND"]},
                        "Mounts": [{"Type": "bind", "Source": str(sync),
                                    "Destination": "/opt/bc_candidate", "RW": False}]}]

            def runner(argv):
                self.assertTrue(diagnose.command_allowed(argv), argv)
                commands.append(argv)
                if argv[0] == "docker":
                    return {"status": "OK", "stdout": json.dumps(inspect)}
                if argv[1] == "list-timers":
                    return {"status": "OK", "stdout": "next 2min ago bc-catalog-sync.timer bc-catalog-sync.service\n"}
                if argv[1] == "show":
                    return {"status": "OK", "stdout": "ActiveState=active\nUnitFileState=enabled\nFragmentPath=/etc/systemd/system/bc-catalog-sync.service\nEnvironmentFiles=/home/ubuntu/bc_sync_20261103/.env (ignore_errors=no)\nExecStart={ path=/usr/bin/python3 ; argv[]=/usr/bin/python3 /home/ubuntu/bc_sync_20261103/sync_catalog.py --secret DO_NOT_PRINT_SYSTEMD_ARGUMENT ; }\n"}
                return {"status": "OK", "stdout": "SHOPIFY_CLIENT_SECRET=" + secrets[1] + "\n*/5 * * * * python3 /home/ubuntu/bc_sync_20261103/sync_catalog.py --token DO_NOT_PRINT_USER_CRON\n"}

            def opener(request, timeout):
                self.assertEqual(timeout, 10)
                self.assertEqual(request.get_method(), "GET")
                self.assertTrue(request.full_url.startswith("http://127.0.0.1:8108/"))
                self.assertEqual(request.get_header("X-typesense-api-key"), secrets[0])
                requests.append(request.full_url)
                if request.full_url.endswith("/aliases"):
                    body = {"aliases": [{"name": "bc_live", "collection_name": "bc_sync_20261103t120045_4e7799"}]}
                elif "/documents/search?" in request.full_url:
                    body = {"hits": [{"document": {"id": "123", "shopify_product_id": "gid://shopify/Product/123",
                             "collection_ids": ["gid://shopify/Collection/456"],
                             "email": "DO_NOT_PRINT_CUSTOMER@example.com", "token": secrets[0]}}]}
                else:
                    body = {"name": "bc_sync_20261103t120045_4e7799", "num_documents": 11679,
                            "fields": [{"name": "title", "type": "string"},
                                       {"name": "f_kleur", "type": "string", "facet": True}]}
                return FakeResponse(json.dumps(body).encode())

            report = diagnose.build_report(runner, {"SHOPIFY_ADMIN_ACCESS_TOKEN": secrets[3]}, opener,
                                           home, opt, etc)
            raw = json.dumps(report)
            for secret in [*secrets, "DO_NOT_PRINT_SOURCE_LITERAL", "DO_NOT_PRINT_CRON_ARGUMENT",
                           "DO_NOT_PRINT_DOCKER_COMMAND", "DO_NOT_PRINT_SYSTEMD_ARGUMENT",
                           "DO_NOT_PRINT_USER_CRON", "DO_NOT_PRINT_CUSTOMER@example.com"]:
                self.assertNotIn(secret, raw)
            self.assertTrue(report["read_only"])
            self.assertFalse(report["writes_performed"])
            self.assertEqual(report["typesense"]["document_count"], 11679)
            self.assertEqual(report["typesense"]["sample_identity_formats"]["shopify_product_id"], "shopify_gid")
            self.assertEqual(report["typesense"]["sample_identity_formats"]["id"], "numeric_string")
            self.assertEqual(len(report["typesense"]["aliases"]), 1)
            self.assertTrue(any(x["path"].endswith("sync_catalog.py") for x in report["runtime_files"]["scripts"]))
            self.assertTrue(report["runtime_files"]["env_files"][0]["credentials"][0]["present"])
            self.assertTrue(report["jobs"]["cron_jobs"])
            self.assertEqual(len(requests), 3)

    def test_missing_key_stops_typesense_reads(self):
        redactor = diagnose.Redactor()
        def forbidden(*args, **kwargs):
            self.fail("No HTTP request may be sent without an existing key")
        result = diagnose.typesense_report({"TYPESENSE_COLLECTION": "bc_live"}, redactor, forbidden)
        self.assertEqual(result["status"], "NO_UNAMBIGUOUS_EXISTING_KEY")

    def test_diagnostic_command_allowlist_refuses_mutations(self):
        for command in [["docker", "restart", diagnose.CONTAINER],
                        ["systemctl", "restart", "bc-sync.service"],
                        ["crontab", "-r"], ["sh", "-c", "env"],
                        ["docker", "inspect", "other-container"]]:
            with patch.object(diagnose.subprocess, "run") as run:
                self.assertEqual(diagnose.run_command(command)["status"], "COMMAND_REFUSED")
                run.assert_not_called()
        with patch.object(diagnose.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, "ok")) as run:
            self.assertEqual(diagnose.run_command(["docker", "inspect", diagnose.CONTAINER])["status"], "OK")
            self.assertEqual(run.call_args.kwargs["timeout"], 10)

    def test_raw_command_errors_and_http_bodies_are_hidden(self):
        with patch.object(diagnose.subprocess, "run", return_value=subprocess.CompletedProcess([], 1, "PRIVATE_STDOUT", "PRIVATE_STDERR")):
            result = diagnose.run_command(["docker", "inspect", diagnose.CONTAINER])
            self.assertNotIn("PRIVATE", json.dumps(result))
        def denied(request, timeout):
            raise HTTPError(request.full_url, 401, "PRIVATE_TOKEN", {}, None)
        result = diagnose.local_json("/aliases", "PRIVATE_TOKEN", denied)
        self.assertEqual(result, (None, "HTTP_401"))
        def failed(request, timeout):
            raise URLError("PRIVATE_URL_OR_TOKEN")
        self.assertEqual(diagnose.local_json("/aliases", "PRIVATE_TOKEN", failed), (None, "CONNECTION_FAILED"))

    def test_metadata_values_are_redacted_even_inside_paths(self):
        redactor = diagnose.Redactor()
        redactor.register({"TYPESENSE_API_KEY": "PRIVATE_LONG_TOKEN"})
        self.assertEqual(redactor.clean({"mount": "/opt/PRIVATE_LONG_TOKEN/data"}), {"mount": "/opt/[REDACTED]/data"})

    def test_scan_does_not_follow_symlinks_or_print_script_bodies(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); source = root / "bc_sync"; source.mkdir()
            outside = root / "outside"; outside.mkdir()
            (outside / "sync_private.py").write_text("NEVER_SCAN_OUTSIDE\n")
            (source / "linked").symlink_to(outside, target_is_directory=True)
            (source / "sync_catalog.py").write_text("PRIVATE_SOURCE_BODY\n")
            result = diagnose.scan_runtime_files([source], diagnose.Redactor())
            raw = json.dumps(result)
            self.assertNotIn("NEVER_SCAN_OUTSIDE", raw)
            self.assertNotIn("PRIVATE_SOURCE_BODY", raw)
            self.assertEqual(len(result["scripts"]), 1)
            self.assertEqual(len(result["scripts"][0]["sha256"]), 64)

    def test_collection_name_cannot_change_the_fixed_http_target(self):
        for name in ["../private", "https://attacker.example", "", "a/b"]:
            result = diagnose.typesense_report({"TYPESENSE_COLLECTION": name, "TYPESENSE_API_KEY": "PRIVATE_LONG_TOKEN"}, diagnose.Redactor())
            self.assertEqual(result["status"], "NO_VALID_COLLECTION_NAME")

    def test_only_known_read_routes_can_receive_a_local_key(self):
        def forbidden(*args, **kwargs):
            self.fail("Refused route must not reach the HTTP client")
        for path in ["/keys", "/aliases/secret", "/collections/x/documents/import",
                     "/collections/../../keys", "//attacker.example/"]:
            self.assertEqual(diagnose.local_json(path, "PRIVATE_LONG_TOKEN", forbidden),
                             (None, "URL_REFUSED"))


if __name__ == "__main__":
    unittest.main()
