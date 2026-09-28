class Discount:

    def __init__(self, description: str, percent: float | int):
        self.description = description
        self.percent = percent

    def __str__(self):
        return f"Скидка (Описание={self.description}, процент скидки={self.percent})"

    def __repr__(self):
        return f"Скидка (Описание={self.description!r}, процент скидки={self.percent})"

    @staticmethod
    def calculate_discounted_price(self, price: float) -> float:
        return price * (100 - self.percent) / 100