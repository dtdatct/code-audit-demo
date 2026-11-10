from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("search_products", __name__)


@bp.route("/search", methods=['GET'])
def search_products():
    q = request.args.get("q", "")
    conn = get_conn()
    rows = conn.execute(f"SELECT id, name, price FROM products WHERE name LIKE '%{q}%'").fetchall()
    return jsonify([dict(r) for r in rows])
