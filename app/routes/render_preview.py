from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("render_preview", __name__)


@bp.route("/preview", methods=['POST'])
def render_preview():
    tpl = request.form.get("template", "Hi")
    return render_template_string(tpl)
