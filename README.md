# Store Order API

A small FastAPI service that records store orders and reports total revenue.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload      # open http://127.0.0.1:8000/docs
pytest -v                      # 8 tests
```

## Endpoints

| Method | Path | What it does |
|---|---|---|
| POST | /orders | Adds an order (product, quantity, unit_price) and returns its total |
| GET | /orders/summary | Returns the number of orders and the total revenue |
| DELETE | /orders | Clears all orders |

## Example Request

`POST /orders`

```json
{ "product": "Notebook", "quantity": 3, "unit_price": 10.0 }
```

Response:

```json
{ "product": "Notebook", "quantity": 3, "unit_price": 10.0, "total": 30.0 }
```

## Model

`OrderItem` in `models.py` is a standard Python dataclass with the fields `product`, `quantity` and `unit_price`, and a `total` property (quantity × unit_price).
