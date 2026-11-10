from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
import yaml

bp = Blueprint("import_config", __name__)


@bp.route("/config/import", methods=['POST'])
def import_config():
    doc = yaml.load(request.data)
    return jsonify(doc)
