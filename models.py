from dataclasses import dataclass


# Order item stored as a standard dataclass.
# Type hints look correct, but nothing checks them at runtime.
@dataclass
class OrderItem:
    product: str
    quantity: int
    unit_price: float

    @property
    def total(self):
        return self.quantity * self.unit_price
