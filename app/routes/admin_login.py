from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("admin_login", __name__)


@bp.route("/admin/login", methods=['POST'])
def admin_login():
    if request.form.get("password") == "admin123":
        return jsonify(token="ADMIN-STATIC-TOKEN")
    return jsonify(error="denied"), 403
