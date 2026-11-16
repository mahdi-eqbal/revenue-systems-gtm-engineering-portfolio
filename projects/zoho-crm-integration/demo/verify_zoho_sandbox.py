"""Verify OAuth access to the EU Zoho CRM Sandbox without saving credentials."""

import hmac
import json
import secrets
import sys
import time
import webbrowser
from getpass import getpass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

ACCOUNTS = "https://accounts.zoho.eu"
SANDBOX = "https://sandbox.zohoapis.eu"
REDIRECT = "http://localhost:8765/oauth/callback"


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def read_json(request):
    stage = "token exchange" if urlsplit(request.full_url).netloc == "accounts.zoho.eu" else "Sandbox API"
    try:
        with build_opener(ProxyHandler({}), NoRedirect()).open(request, timeout=20) as response:
            payload = json.load(response)
    except HTTPError as error:
        body = error.read(16384)
        try:
            payload = json.loads(body)
        except ValueError:
            payload = {}
        detail = safe_error(payload)
        if not payload:
            page = body.lower()
            reason = next(
                (label for phrase, label in (
                    (b"request header or cookie too large", "headers too large"),
                    (b"request rejected", "request rejected"),
                    (b"access denied", "access denied"),
                    (b"invalid request", "invalid request"),
                    (b"bad request", "bad request page"),
                ) if phrase in page),
                "unrecognized response",
            )
            detail = f"{error.headers.get_content_type()}; {reason}"
        raise RuntimeError(f"{stage}: HTTP {error.code}; {detail}") from None
    if "error" in payload:
        raise RuntimeError(f"{stage}: {safe_error(payload)}")
    return payload


def safe_error(payload):
    code = payload.get("error") or payload.get("code")
    known = {
        "invalid_client", "invalid_client_secret", "invalid_code", "invalid_grant",
        "invalid_redirect_uri", "INVALID_TOKEN", "OAUTH_SCOPE_MISMATCH",
        "INVALID_URL_PATTERN", "NO_PERMISSION", "INVALID_DATA", "INVALID_REQUEST",
    }
    return code if isinstance(code, str) and code in known else "no recognized Zoho error code"


def token_request(fields):
    boundary = secrets.token_hex(24)
    parts = [
        f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n{value}\r\n'
        for name, value in fields.items()
    ]
    body = ("".join(parts) + f"--{boundary}--\r\n").encode()
    return Request(f"{ACCOUNTS}/oauth/v2/token", data=body, headers={
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "User-Agent": "CRM-Lead-Integration/1.0",
    })

def verify():
    client_id = input("Client ID: ").strip()
    client_secret = getpass("Client Secret (hidden): ").strip()
    if not client_id or not client_secret:
        raise RuntimeError("Both client credentials are required.")

    if "--self-client" in sys.argv:
        code = getpass("Self Client grant code (hidden): ").strip()
        if not code:
            raise RuntimeError("A fresh Sandbox grant code is required.")
        verify_token(client_id, client_secret, code, self_client=True)
        return

    state = secrets.token_urlsafe(32)
    callback = {}

    class CallbackHandler(BaseHTTPRequestHandler):
        def log_message(self, *_args):
            pass

        def do_GET(self):
            parsed = urlsplit(self.path)
            fields = parse_qs(parsed.query)
            valid = parsed.path == "/oauth/callback" and hmac.compare_digest(
                fields.get("state", [""])[0], state
            )
            if valid:
                callback.update(fields)
            self.send_response(200 if valid else 400)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Referrer-Policy", "no-referrer")
            self.end_headers()
            reply = "Return to the command window for the result." if valid else "Invalid callback."
            self.wfile.write(reply.encode())

    with ThreadingHTTPServer(("127.0.0.1", 8765), CallbackHandler) as server:
        server.timeout = 1
        query = urlencode({
            "client_id": client_id,
            "response_type": "code",
            "scope": ("ZohoCRM.org.READ,ZohoCRM.modules.leads.CREATE,ZohoCRM.modules.leads.READ" if "--smoke-lead" in sys.argv else "ZohoCRM.org.READ"),
            "redirect_uri": REDIRECT,
            "access_type": "online",
            "state": state,
        })
        print("In Zoho, select Sandbox > Zoho CRM Integration and approve read access.")
        if not webbrowser.open(f"{ACCOUNTS}/oauth/v2/auth?{query}"):
            raise RuntimeError("Could not open the browser.")
        deadline = time.monotonic() + 300
        while not callback and time.monotonic() < deadline:
            server.handle_request()

    code = callback.get("code", [""])[0]
    if not code:
        raise RuntimeError("Authorization was declined or timed out.")

    verify_token(client_id, client_secret, code)


def verify_token(client_id, client_secret, code, *, self_client=False):
    fields = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
    }
    if not self_client:
        fields["redirect_uri"] = REDIRECT
    token = read_json(token_request(fields))
    if not token.get("access_token"):
        raise RuntimeError("Zoho did not issue an access token. Check the client credentials.")
    if token.get("api_domain") != SANDBOX:
        raise RuntimeError("Zoho authorized a different environment. Select the EU Sandbox.")

    org = read_json(Request(f"{SANDBOX}/crm/v8/org", headers={
        "Authorization": f"Zoho-oauthtoken {token['access_token']}"
    })).get("org", [])
    if len(org) != 1 or org[0].get("type") != "sandbox":
        raise RuntimeError("The organization could not be verified as a Sandbox.")
    print("Sandbox connection verified. No credentials were saved.")
    if "--smoke-lead" in sys.argv:
        from sandbox_smoke import check_lead
        print(check_lead(org[0], token["access_token"], read_json))


if __name__ == "__main__":
    try:
        verify()
    except HTTPError as error:
        raise SystemExit(f"Zoho returned HTTP {error.code}.")
    except (RuntimeError, URLError, OSError, ValueError, KeyboardInterrupt) as error:
        if isinstance(error, RuntimeError):
            raise SystemExit(str(error))
        raise SystemExit("Connection check interrupted or unavailable.")








