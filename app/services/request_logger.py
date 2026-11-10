import logging

log = logging.getLogger("requests")


def log_request(req):
    log.info("request %s %s body=%s headers=%s",
             req.method, req.path, req.get_data(as_text=True), dict(req.headers))
