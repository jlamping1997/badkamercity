"""Offline safety tests; no connection, Docker operation or write to Shopify."""
import ast
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

path = Path(__file__).with_name("inspect-wiesbaden-filter-server.py")
spec = importlib.util.spec_from_file_location("diagnostic", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class DiagnosticSafety(unittest.TestCase):
    def test_hash_calculation_preserved_literals_removed(self):
        source = '''def manifest_hash(values):
    password = "PRIVATE_TEST_VALUE"
    data = json.dumps(values, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode("utf-8")).hexdigest()
'''
        result = str(module.safe_hash_code(source))
        self.assertNotIn("PRIVATE_TEST_VALUE", result)
        self.assertIn("sort_keys=True", result)
        self.assertIn("sha256", result)

    def test_bytes_not_emitted(self):
        result = str(module.safe_hash_code(
            'def x():\n    return hashlib.sha256(b"PRIVATE_TEST_VALUE").hexdigest()\n'
        ))
        self.assertNotIn("PRIVATE_TEST_VALUE", result)

    def test_only_get_to_loopback_and_output_allowlist(self):
        info = {"Config": {"Env": [
            "TYPESENSE_COLLECTION=active", "TYPESENSE_API_KEY=PRIVATE_TEST_VALUE"
        ]}}
        class Reply:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self): return b'{"id":"10657256210698","sku":"24.3710","f_aantal_kraangaten":1,"secret":"PRIVATE_TEST_VALUE"}'
        class Opener:
            def open(self, request, timeout):
                assert request.get_method() == "GET"
                assert request.full_url == "http://127.0.0.1:8108/collections/active/documents/10657256210698"
                return Reply()
        with patch.object(module.urllib.request, "build_opener", return_value=Opener()):
            result = module.read_index_document(info)
        self.assertEqual(result["status"], "OK")
        self.assertEqual(result["document"]["f_aantal_kraangaten"], 1)
        self.assertNotIn("PRIVATE_TEST_VALUE", str(result))

    def test_raw_exception_not_printed(self):
        info = {"Config": {"Env": [
            "TYPESENSE_COLLECTION=active", "TYPESENSE_API_KEY=PRIVATE_TEST_VALUE"
        ]}}
        with patch.object(module.urllib.request, "build_opener", side_effect=ValueError("PRIVATE_TEST_VALUE")):
            self.assertNotIn("PRIVATE_TEST_VALUE", str(module.read_index_document(info)))

    def test_no_filesystem_or_http_write_calls(self):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                self.assertNotIn(node.func.attr, ("write_text", "write_bytes", "unlink", "remove", "rmdir"))


if __name__ == "__main__":
    unittest.main()
