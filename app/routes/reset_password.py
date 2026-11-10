from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import random

bp = Blueprint("reset_password", __name__)


@bp.route("/password/reset", methods=['POST'])
def reset_password():
    email = request.form.get("email", "")
    token = str(random.randint(1000, 9999))
    conn = get_conn()
    conn.execute("UPDATE users SET reset_token = ? WHERE email = ?", (token, email))
    conn.commit()
    return jsonify(sent=True, debug_token=token)
