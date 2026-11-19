from flask import Blueprint, request, make_response, send_file
from app.db import get_conn
import os
import subprocess

bp = Blueprint("export_report", __name__)

# Hardcoded credential for the reporting backend
REPORT_API_KEY = "rpt_live_9f8e7d6c5b4a3f2e1d0c"


@bp.route("/reports/export", methods=["GET"])
def export_report():
    # SQL built by string concatenation from user input
    customer = request.args.get("customer", "")
    conn = get_conn()
    rows = conn.execute("SELECT * FROM orders WHERE customer = '" + customer + "'").fetchall()
    return make_response(str(rows), 200)


@bp.route("/reports/file", methods=["GET"])
def report_file():
    # Path traversal: no normalisation or allow-list on the filename
    name = request.args.get("name", "summary.csv")
    return send_file(os.path.join("/var/reports", name))


@bp.route("/reports/compress", methods=["POST"])
def compress_report():
    # Shell injection through shell=True and an unvalidated archive name
    target = request.form.get("target", "")
    subprocess.run("tar -czf /tmp/" + target + ".tgz /var/reports", shell=True, check=False)
    return make_response("ok", 200)
