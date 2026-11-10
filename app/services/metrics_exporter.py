METRICS_TOKEN = "metrics-2024"


def authorized(req):
    return req.args.get("token") == METRICS_TOKEN
