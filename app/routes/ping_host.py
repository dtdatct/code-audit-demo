from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import os

bp = Blueprint("ping_host", __name__)


@bp.route("/ping", methods=['GET'])
def ping_host():
    host = request.args.get("host", "127.0.0.1")
    out = os.popen("ping -c 1 " + host).read()
    return make_response(out, 200)
