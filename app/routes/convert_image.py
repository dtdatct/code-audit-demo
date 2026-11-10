from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import subprocess

bp = Blueprint("convert_image", __name__)


@bp.route("/convert", methods=['POST'])
def convert_image():
    src = request.form.get("src", "")
    fmt = request.form.get("fmt", "png")
    subprocess.call(f"convert {src} out.{fmt}", shell=True)
    return jsonify(status="ok")
