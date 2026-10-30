from dataclasses import asdict

from fastapi import FastAPI

from models import OrderItem

app = FastAPI(title="Store Order API")

orders: list[OrderItem] = []


@app.post("/orders", status_code=201)
def create_order(data: dict):
    # Raw JSON is passed straight into the dataclass
    item = OrderItem(**data)
    orders.append(item)
    return {**asdict(item), "total": item.total}


@app.get("/orders/summary")
def order_summary():
    return {
        "count": len(orders),
        "revenue": sum(item.total for item in orders),
    }


@app.delete("/orders")
def clear_orders():
    orders.clear()
    return {"cleared": True}
