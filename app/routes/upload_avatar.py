from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import os

bp = Blueprint("upload_avatar", __name__)


@bp.route("/avatar", methods=['POST'])
def upload_avatar():
    f = request.files["avatar"]
    path = os.path.join("/srv/static/avatars", f.filename)
    f.save(path)
    return jsonify(path=path)
