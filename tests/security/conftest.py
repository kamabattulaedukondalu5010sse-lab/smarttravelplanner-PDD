import os
import sys
import json
import pytest
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

REPORTS_DIR = os.path.join(BASE_DIR, "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

@pytest.fixture(scope="session")
def repo_root():
    return REPO_ROOT

@pytest.fixture(scope="session")
def target_url():
    target = os.getenv("SECURITY_TEST_TARGET") or os.getenv("BASE_URL") or "http://127.0.0.1:5000"
    return target.rstrip("/")

@pytest.fixture(scope="session")
def valid_auth_token(target_url):
    """
    Attempts to get token from live target, otherwise returns simulated token for offline testing.
    """
    try:
        res = requests.post(
            f"{target_url}/api/auth/login",
            json={"email": "john@example.com", "password": "anypassword"},
            timeout=3
        )
        if res.status_code == 200:
            return res.json().get("token", "mock_sec_token_12345")
    except Exception:
        pass
    return "mock_sec_token_12345"

@pytest.fixture(scope="session")
def auth_headers(valid_auth_token):
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {valid_auth_token}"
    }
