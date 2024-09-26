import secrets
import time
from typing import Dict, Optional

# Hardcoded test user
TEST_USER = {
    "username": "testuser",
    "password": "testpassword"
}

# In-memory token storage
tokens: Dict[str, int] = {}


def generate_token() -> str:
    return secrets.token_urlsafe(32)


def create_access_token(username: str) -> str:
    token = generate_token()
    tokens[token] = int(time.time()) + 3600  # Token expires in 1 hour
    return token


def verify_token(token: str) -> Optional[str]:
    expiration = tokens.get(token)
    if expiration is None:
        return None
    if int(time.time()) > expiration:
        tokens.pop(token, None)
        return None
    return TEST_USER["username"]


def authenticate_user(username: str, password: str) -> bool:
    return username == TEST_USER["username"] and password == TEST_USER["password"]
