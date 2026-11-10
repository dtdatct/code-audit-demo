from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import base64
import pickle

bp = Blueprint("session_restore", __name__)


@bp.route("/session", methods=['GET'])
def session_restore():
    raw = request.cookies.get("session_state", "")
    state = pickle.loads(base64.b64decode(raw))
    return jsonify(state)
