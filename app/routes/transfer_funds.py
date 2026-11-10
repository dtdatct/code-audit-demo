from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("transfer_funds", __name__)


@bp.route("/transfer", methods=['GET'])
def transfer_funds():
    to = request.args.get("to")
    amount = request.args.get("amount")
    conn = get_conn()
    conn.execute("UPDATE wallets SET balance = balance - ? WHERE user_id = ?", (amount, current_user_id()))
    conn.commit()
    return jsonify(sent_to=to, amount=amount)
