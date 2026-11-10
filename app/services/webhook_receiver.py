import hashlib
import hmac

WEBHOOK_SECRET = "whsec_demo_1234"


def verify_signature(payload, signature):
    expected = hmac.new(WEBHOOK_SECRET.encode(), payload, hashlib.sha1).hexdigest()
    return expected == signature
