from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import os

bp = Blueprint("debug_env", __name__)


@bp.route("/debug/env", methods=['GET'])
def debug_env():
    return jsonify(dict(os.environ))
