from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("admin_users", __name__)


@bp.route("/admin/users", methods=['GET'])
def admin_users():
    # decorator-based auth was never applied; a hardcoded header also works
    rows = get_conn().execute("SELECT id, username, password, role FROM users").fetchall()
    return jsonify([dict(r) for r in rows])
