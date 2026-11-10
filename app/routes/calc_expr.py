from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("calc_expr", __name__)


@bp.route("/calc", methods=['GET'])
def calc_expr():
    expr = request.args.get("expr", "0")
    return jsonify(result=eval(expr))
