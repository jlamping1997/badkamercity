"""Offline checks for safe Shopify Dev Dashboard authentication."""
import io
import json
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import parse_qs
import importlib.util
import unittest
from unittest.mock import Mock

spec = importlib.util.spec_from_file_location("shopify_auth", Path(__file__).with_name("shopify_auth.py"))
auth = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auth)
SHOP = "fpa9hu-i3.myshopify.com"


class FakeResponse:
    def __init__(self, url, payload):
        self.url = url
        self.body = json.dumps(payload).encode()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def geturl(self):
        return self.url

    def read(self, limit=None):
        return self.body[:limit]


class TokenTests(unittest.TestCase):
    def test_existing_token_requires_no_network(self):
        opener = Mock(side_effect=AssertionError("Should not use network"))
        self.assertEqual(auth.get_shopify_token(SHOP, {"SHOPIFY_ADMIN_ACCESS_TOKEN": " token "}, opener), "token")
        opener.assert_not_called()

    def test_no_credentials_stops_safely(self):
        with self.assertRaisesRegex(ValueError, "not configured"):
            auth.get_shopify_token(SHOP, {}, Mock())

    def test_partial_credentials_stops_safely(self):
        with self.assertRaisesRegex(ValueError, "not configured"):
            auth.get_shopify_token(SHOP, {"SHOPIFY_CLIENT_ID": "client"}, Mock())

    def test_credentials_grant_uses_shopify_fixed_url(self):
        def opener(req, timeout):
            self.assertEqual(timeout, 25)
            self.assertEqual(req.full_url, f"https://{SHOP}/admin/oauth/access_token")
            self.assertEqual(req.get_method(), "POST")
            self.assertEqual(req.get_header("Content-type"), "application/x-www-form-urlencoded")
            values = parse_qs(req.data.decode())
            self.assertEqual(values["grant_type"], ["client_credentials"])
            self.assertEqual(values["client_id"], ["client"])
            self.assertEqual(values["client_secret"], ["secret"])
            return FakeResponse(req.full_url, {"access_token": "new-token", "expires_in": 86399})
        self.assertEqual(auth.get_shopify_token(SHOP, {"SHOPIFY_CLIENT_ID": "client", "SHOPIFY_CLIENT_SECRET": "secret"}, opener), "new-token")

    def test_unknown_shop_fails_without_network(self):
        op = Mock()
        with self.assertRaisesRegex(ValueError, "Unexpected Shopify shop"):
            auth.get_shopify_token("other.myshopify.com", {"SHOPIFY_CLIENT_ID":"x","SHOPIFY_CLIENT_SECRET":"y"}, op)
        op.assert_not_called()

    def test_http_errors_do_not_disclose_secrets(self):
        def opener(req, timeout):
            raise HTTPError(req.full_url, 401, "unauthorized", hdrs=None, fp=io.BytesIO(b'bad secret'))
        with self.assertRaises(RuntimeError) as caught:
            auth.get_shopify_token(SHOP, {"SHOPIFY_CLIENT_ID":"client", "SHOPIFY_CLIENT_SECRET":"private-secret"}, opener)
        self.assertIn("HTTP 401", str(caught.exception))
        self.assertNotIn("private-secret", str(caught.exception))

    def test_reject_missing_token(self):
        with self.assertRaisesRegex(RuntimeError, "no access token"):
            auth.get_shopify_token(SHOP, {"SHOPIFY_CLIENT_ID":"a", "SHOPIFY_CLIENT_SECRET":"b"}, lambda req, timeout: FakeResponse(req.full_url, {"scope":"read_products"}))

    def test_reject_redirected_response(self):
        with self.assertRaisesRegex(RuntimeError, "redirected"):
            auth.get_shopify_token(SHOP, {"SHOPIFY_CLIENT_ID":"a", "SHOPIFY_CLIENT_SECRET":"b"}, lambda req, timeout: FakeResponse("https://example.com/", {"access_token":"token"}))


if __name__ == "__main__":
    unittest.main()
