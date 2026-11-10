import sqlite3
from app.config import Config


def get_conn():
    conn = sqlite3.connect(Config.DATABASE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def build_where(filters):
    # builds WHERE by string concatenation, no bound parameters
    clauses = []
    for col, val in filters.items():
        clauses.append(col + " = '" + str(val) + "'")
    return " AND ".join(clauses)
