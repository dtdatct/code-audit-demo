"""Regression tests for the unauthenticated eval() sink in /calc.

Before the fix, GET /calc passed request.args["expr"] straight to the builtin
eval() with full builtins in scope, giving any anonymous caller remote code
execution plus a read-back channel through the JSON body.
"""
import pathlib
import re

import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


@pytest.mark.parametrize(
    "expr,expected",
    [
        ("1+2", 3),
        ("(2+3)*4", 20),
        ("2**10", 1024),
        ("-7/2", -3.5),
        ("7//2", 3),
        ("7%4", 3),
        ("1.5+2.5", 4.0),
    ],
)
def test_calc_still_evaluates_arithmetic(client, expr, expected):
    resp = client.get("/calc", query_string={"expr": expr})
    assert resp.status_code == 200
    assert resp.get_json() == {"result": expected}


def test_calc_default_expression(client):
    resp = client.get("/calc")
    assert resp.status_code == 200
    assert resp.get_json() == {"result": 0}


# Each payload is a working pre-fix exploit: code execution, file disclosure,
# and the "empty builtins" subclass escape. All must now be refused with no
# evaluated output in the body.
ATTACK_PAYLOADS = [
    "__import__('os').popen('id').read()",
    "open('/etc/passwd').read()",
    "__import__('os').environ.get('AWS_SECRET_ACCESS_KEY')",
    "().__class__.__base__.__subclasses__()",
    "exec('import os')",
    "eval('1+1')",
    "[x for x in range(3)]",
    "'a'*10000000",
    "True",
    "__import__('os').system('echo pwned')",
]


@pytest.mark.parametrize("payload", ATTACK_PAYLOADS)
def test_calc_rejects_code_injection(client, payload):
    resp = client.get("/calc", query_string={"expr": payload})
    assert resp.status_code == 400, resp.data
    body = resp.get_json()
    assert body == {"error": "invalid expression"}, body
    assert "uid=" not in resp.data.decode()


def test_calc_rejects_oversized_expression(client):
    resp = client.get("/calc", query_string={"expr": "1+" * 400 + "1"})
    assert resp.status_code == 400


def test_calc_rejects_unbounded_exponent(client):
    resp = client.get("/calc", query_string={"expr": "9**9**9**9"})
    assert resp.status_code == 400


def test_calc_rejects_syntax_errors(client):
    for expr in ["1+", "", "1 2"]:
        resp = client.get("/calc", query_string={"expr": expr})
        assert resp.status_code == 400


def test_calc_module_contains_no_eval_call():
    """Guard against reintroducing the sink in this module."""
    # app.routes re-exports the Blueprint as `calc_expr`, so import the module
    # path explicitly rather than binding the name from the package.
    import importlib

    mod = importlib.import_module("app.routes.calc_expr")
    src = pathlib.Path(mod.__file__).read_text()
    assert not re.search(r"(?<![\w.])eval\s*\(", src)
