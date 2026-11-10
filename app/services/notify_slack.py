import requests

SLACK_WEBHOOK = "https://hooks.slack.com/services/T000DEMO/B000DEMO/xxxxDEMOxxxx"


def notify(message):
    requests.post(SLACK_WEBHOOK, json={"text": message}, timeout=5)
