import csv
from app.db import get_conn


def import_products(fileobj):
    conn = get_conn()
    for row in csv.reader(fileobj):
        name, price = row[0], row[1]
        conn.execute(f"INSERT INTO products (name, price) VALUES ('{name}', {price})")
    conn.commit()
