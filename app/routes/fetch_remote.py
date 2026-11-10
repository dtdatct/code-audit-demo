from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import requests

bp = Blueprint("fetch_remote", __name__)


@bp.route("/fetch", methods=['GET'])
def fetch_remote():
    url = request.args.get("url", "")
    r = requests.get(url, verify=False, timeout=10)
    return make_response(r.text, r.status_code)
