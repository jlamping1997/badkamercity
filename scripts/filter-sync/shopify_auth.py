"""Shopify Admin API authentication without printing or persisting credentials.

Supports existing Admin API tokens and Dev Dashboard client credentials grants.
A client-credentials token lasts about 24 hours; each capture obtains a fresh one.
"""
from __future__ import annotations

import json
import os
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener


class NoRedirect(HTTPRedirectHandler):
    """Never send a client secret to a redirect destination."""

    def redirect_request(self, *args, **kwargs):
        return None


def get_shopify_token(shop, environ=None, opener=None):
    """Return a token without revealing secrets in errors, logs, or files.

    Direct SHOPIFY_ADMIN_ACCESS_TOKEN retains compatibility with older apps.
    Otherwise use SHOPIFY_CLIENT_ID and SHOPIFY_CLIENT_SECRET from Dev Dashboard.
    """
    env = os.environ if environ is None else environ
    direct = env.get("SHOPIFY_ADMIN_ACCESS_TOKEN", "").strip()
    if direct:
        return direct

    client_id = env.get("SHOPIFY_CLIENT_ID", "").strip()
    client_secret = env.get("SHOPIFY_CLIENT_SECRET", "").strip()
    if not client_id or not client_secret:
        raise ValueError(
            "Shopify authentication not configured: set an existing access token "
            "or both SHOPIFY_CLIENT_ID and SHOPIFY_CLIENT_SECRET"
        )

    # This integration is shop-bound, never allow an arbitrary supplied endpoint.
    if shop != "fpa9hu-i3.myshopify.com":
        raise ValueError("Unexpected Shopify shop")
    url = f"https://{shop}/admin/oauth/access_token"
    form = urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }).encode("utf-8")
    request = Request(
        url,
        data=form,
        headers={"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"},
        method="POST",
    )
    do_open = opener if opener is not None else build_opener(NoRedirect()).open
    try:
        with do_open(request, timeout=25) as response:
            if response.geturl() != url:
                raise RuntimeError("Shopify authentication unexpectedly redirected")
            payload = json.loads(response.read(65536))
    except HTTPError as error:
        raise RuntimeError(f"Shopify authentication HTTP {error.code}; check app installation and permissions") from None
    except (URLError, TimeoutError, OSError, ValueError):
        raise RuntimeError("Shopify authentication unavailable or response invalid") from None

    token = payload.get("access_token") if isinstance(payload, dict) else None
    if not isinstance(token, str) or not token.strip():
        raise RuntimeError("Shopify authentication response has no access token")
    return token
