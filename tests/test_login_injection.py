"""Regression tests for the login SQL injection (Cyber finding F-0001)."""
import sqlite3

import pytest

from app import create_app
from app.config import Config


@pytest.fixture()
def client(tmp_path, monkeypatch):
    db_path = tmp_path / "shoplite-test.db"
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)")
    conn.execute("INSERT INTO users (id, username, password, role) VALUES (1, 'admin', 's3cret', 'admin')")
    conn.commit()
    conn.close()

    monkeypatch.setattr(Config, "DATABASE", str(db_path))
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_sql_injection_payload_is_not_authenticated(client):
    resp = client.post("/login", data={"username": "' OR 1=1--", "password": "anything"})
    assert resp.status_code == 401
    assert resp.get_json() == {"error": "invalid"}


def test_sql_injection_with_empty_password_is_not_authenticated(client):
    resp = client.post("/login", data={"username": "' OR 1=1--", "password": ""})
    assert resp.status_code == 401


def test_valid_credentials_still_authenticate(client):
    resp = client.post("/login", data={"username": "admin", "password": "s3cret"})
    assert resp.status_code == 200
    assert resp.get_json() == {"id": 1, "role": "admin"}


def test_wrong_password_is_rejected(client):
    resp = client.post("/login", data={"username": "admin", "password": "wrong"})
    assert resp.status_code == 401
