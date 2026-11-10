from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("update_profile", __name__)


@bp.route("/profile", methods=['PUT'])
def update_profile():
    data = request.get_json(force=True)
    conn = get_conn()
    for k, v in data.items():
        conn.execute(f"UPDATE users SET {k} = ? WHERE id = ?", (v, current_user_id()))
    conn.commit()
    return jsonify(ok=True)
