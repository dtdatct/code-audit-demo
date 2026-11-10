from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("go_redirect", __name__)


@bp.route("/go", methods=['GET'])
def go_redirect():
    nxt = request.args.get("next", "/")
    return redirect(nxt)
