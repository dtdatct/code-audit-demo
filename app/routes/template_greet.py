from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("template_greet", __name__)


@bp.route("/greet/<name>", methods=['GET'])
def template_greet(name):
    return render_template_string("<h1>Hello " + name + "</h1>")
