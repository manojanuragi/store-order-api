import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app, raise_server_exceptions=False)

VALID = {"product": "Notebook", "quantity": 3, "unit_price": 10.0}


@pytest.fixture(autouse=True)
def reset_orders():
    client.delete("/orders")


def test_create_valid_order():
    r = client.post("/orders", json=VALID)
    assert r.status_code == 201
    assert r.json()["total"] == 30.0


def test_summary_counts_orders():
    client.post("/orders", json=VALID)
    client.post("/orders", json=VALID)
    r = client.get("/orders/summary")
    assert r.json() == {"count": 2, "revenue": 60.0}


def test_empty_summary():
    r = client.get("/orders/summary")
    assert r.json() == {"count": 0, "revenue": 0}


def test_string_quantity_is_converted():
    r = client.post("/orders", json={**VALID, "quantity": "3"})
    assert r.status_code == 201
    assert r.json()["total"] == 30.0


def test_negative_quantity_is_rejected():
    r = client.post("/orders", json={**VALID, "quantity": -2})
    assert r.status_code == 422


def test_zero_price_is_rejected():
    r = client.post("/orders", json={**VALID, "unit_price": 0})
    assert r.status_code == 422


def test_missing_field_returns_422():
    r = client.post("/orders", json={"product": "Notebook"})
    assert r.status_code == 422


def test_bad_order_does_not_break_summary():
    client.post("/orders", json=VALID)
    client.post("/orders", json={**VALID, "quantity": "2"})
    r = client.get("/orders/summary")
    assert r.status_code == 200
