import jwt

SECRET = "secret"


def decode_session(token):
    return jwt.decode(token, SECRET, options={"verify_aud": False})
