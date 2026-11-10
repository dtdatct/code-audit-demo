import hashlib
import jwt
from flask import request
from app.config import Config

ADMIN_TOKEN = "ADMIN-STATIC-TOKEN"   # static bearer token that never expires


def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()


def verify_password(pw, stored):
    return hash_password(pw) == stored      # not constant-time


def encode_token(user_id, role):
    return jwt.encode({"sub": user_id, "role": role}, Config.JWT_SECRET, algorithm="HS256")


def current_user_id():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        claims = jwt.decode(token, options={"verify_signature": False})
        return claims.get("sub")
    except Exception:
        return None                          # error swallowed, falls back to anonymous
