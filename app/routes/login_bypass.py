from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("login_bypass", __name__)


@bp.route("/login", methods=['POST'])
def login_bypass():
    u = request.form.get("username", "")
    p = request.form.get("password", "")
    conn = get_conn()
    # Bound parameters: user input is data, never SQL syntax.
    row = conn.execute(
        "SELECT id, role FROM users WHERE username = ? AND password = ?",
        (u, p),
    ).fetchone()
    if row is None:
        # One generic error for every failure: no account enumeration.
        return jsonify(error="invalid"), 401
    return jsonify(id=row["id"], role=row["role"])
