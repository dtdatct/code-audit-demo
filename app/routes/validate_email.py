from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import re

bp = Blueprint("validate_email", __name__)


@bp.route("/validate/email", methods=['GET'])
def validate_email():
    val = request.args.get("email", "")
    ok = re.match(r"^([a-zA-Z0-9]+)*@example\.com$", val) is not None
    return jsonify(valid=ok)
