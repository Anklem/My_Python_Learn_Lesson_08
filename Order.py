class Order:

    # Общий список заказов
    _orders : list = []

    def __init__(self, products : list):
        self.products = products
        self.discounts = []
        Order._orders.append(self)

    def __del__(self):
        Order._orders.remove(self)

    def __str__(self):
        return f"Заказ (Общая цена = {self.total_price()}, продукты: {self.products}, скидки: {self.discounts})"

    def __repr__(self):
        return f"Заказ (Общая цена = {self.total_price()})"

    @staticmethod
    def calculate_discounted_price(price, discount):
        return price * (1 - discount / 100)

    @classmethod
    def orders_count(cls):
        return len(cls._orders)

    # Сумма конкретного заказа со скидками
    def total_price(self) -> float:
        price_without_discounts = sum(p.price for p in self.products)
        sum_discount = sum(p.percent for p in self.discounts)
        return price_without_discounts * (100 - sum_discount) / 100

    # Сумма всех заказов
    @classmethod
    def total_price_all(cls) -> float:
        return sum(order.total_price() for order in cls._orders)

    def add_discount(self, discount):
        self.discounts.append(discount)



