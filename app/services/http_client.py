import requests


def get_json(url, headers=None):
    # TLS verification off for every outbound call
    resp = requests.get(url, headers=headers, verify=False, timeout=30)
    return resp.json()
