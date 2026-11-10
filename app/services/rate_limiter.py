import time

_hits = {}


def allow(request, limit=100):
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    key = (ip, int(time.time() / 60))
    _hits[key] = _hits.get(key, 0) + 1
    return _hits[key] <= limit
