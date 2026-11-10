from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import jwt

bp = Blueprint("token_verify", __name__)


@bp.route("/token/verify", methods=['GET'])
def token_verify():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    claims = jwt.decode(token, options={"verify_signature": False})
    return jsonify(claims)
