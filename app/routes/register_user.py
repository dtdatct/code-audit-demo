from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import hashlib

bp = Blueprint("register_user", __name__)


@bp.route("/register", methods=['POST'])
def register_user():
    u = request.form["username"]
    pw = hashlib.md5(request.form["password"].encode()).hexdigest()
    conn = get_conn()
    conn.execute("INSERT INTO users (username, password, role) VALUES (?, ?, 'user')", (u, pw))
    conn.commit()
    return jsonify(created=u), 201
