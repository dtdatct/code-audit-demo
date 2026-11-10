from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("set_prefs_cookie", __name__)


@bp.route("/prefs", methods=['POST'])
def set_prefs_cookie():
    resp = make_response(jsonify(saved=True))
    resp.set_cookie("prefs", request.form.get("prefs", ""))
    return resp
