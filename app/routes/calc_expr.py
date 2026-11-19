import ast
import operator

from flask import Blueprint, request, jsonify, make_response, redirect, send_file, render_template_string
from app.db import get_conn
from app.auth import current_user_id

bp = Blueprint("calc_expr", __name__)

MAX_EXPR_LENGTH = 200
MAX_EXPONENT = 100

_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

_UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

# Rejections and arithmetic faults both end in a 400: nothing about the
# parsed input is ever evaluated by the interpreter for the caller.
_EVAL_ERRORS = (
    ValueError,
    TypeError,
    SyntaxError,
    RecursionError,
    MemoryError,
    OverflowError,
    ZeroDivisionError,
)


def _eval_node(node):
    """Evaluate an allowlisted arithmetic AST node. Raises ValueError otherwise."""
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant):
        # bool is a subclass of int but is not an arithmetic literal here.
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise ValueError("only numeric literals are allowed")
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _BIN_OPS:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        if isinstance(node.op, ast.Pow) and isinstance(right, int) and abs(right) > MAX_EXPONENT:
            raise ValueError("exponent out of range")
        return _BIN_OPS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPS:
        return _UNARY_OPS[type(node.op)](_eval_node(node.operand))
    raise ValueError("unsupported expression element: " + type(node).__name__)


def safe_arithmetic_eval(expr):
    """Evaluate an arithmetic expression without the builtin evaluator."""
    if not isinstance(expr, str):
        raise ValueError("expression must be a string")
    if len(expr) > MAX_EXPR_LENGTH:
        raise ValueError("expression too long")
    return _eval_node(ast.parse(expr, mode="eval"))


@bp.route("/calc", methods=['GET'])
def calc_expr():
    expr = request.args.get("expr", "0")
    try:
        result = safe_arithmetic_eval(expr)
    except _EVAL_ERRORS:
        return jsonify(error="invalid expression"), 400
    return jsonify(result=result)
