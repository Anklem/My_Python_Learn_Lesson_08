import Order

class Customer:

    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def __str__(self):
        return f"Клиент (Имя={self.name}, Заказы={self.orders})"

    def __repr__(self):
        return f"Клиент (Имя={self.name!r}, Заказы={self.orders})"

    def add_order(self, order: Order.Order):
        self.orders.append(order)
