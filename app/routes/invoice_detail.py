from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("invoice_detail", __name__)


@bp.route("/invoices/<int:invoice_id>", methods=['GET'])
def invoice_detail(invoice_id):
    conn = get_conn()
    row = conn.execute("SELECT * FROM invoices WHERE id = ?", (invoice_id,)).fetchone()
    if row is None:
        return jsonify(error="not found"), 404
    # no check that the invoice belongs to current_user_id()
    return jsonify(dict(row))
