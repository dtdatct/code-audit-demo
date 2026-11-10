from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import logging

bp = Blueprint("auth_log", __name__)


@bp.route("/auth/log", methods=['POST'])
def auth_log():
    logging.getLogger("auth").info("login attempt user=%s password=%s",
                                   request.form.get("username"), request.form.get("password"))
    return jsonify(logged=True)
