from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import os

bp = Blueprint("download_file", __name__)


@bp.route("/download", methods=['GET'])
def download_file():
    name = request.args.get("file", "")
    return send_file(os.path.join("/srv/uploads", name))
