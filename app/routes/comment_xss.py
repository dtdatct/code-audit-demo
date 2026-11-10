from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("comment_xss", __name__)


@bp.route("/comments", methods=['POST'])
def comment_xss():
    body = request.form.get("body", "")
    return "<div class='comment'>" + body + "</div>"
