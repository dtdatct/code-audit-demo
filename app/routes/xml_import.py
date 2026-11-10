from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id
from lxml import etree

bp = Blueprint("xml_import", __name__)


@bp.route("/import/xml", methods=['POST'])
def xml_import():
    parser = etree.XMLParser(resolve_entities=True, load_dtd=True, no_network=False)
    doc = etree.fromstring(request.data, parser)
    return jsonify(name=doc.findtext("name"))
