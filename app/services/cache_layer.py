import pickle
import redis

client = redis.Redis(host="10.0.0.5", port=6379)  # no auth, no TLS


def cache_get(key):
    raw = client.get(key)
    return pickle.loads(raw) if raw else None


def cache_set(key, value):
    client.set(key, pickle.dumps(value))
