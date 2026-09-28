from Customer import Customer
from Order import Order
from Product import Product
from Discount import Discount

# Создаем продукты
product1 = Product("Телефон", 1_200)
product2 = Product("Винтовка", 10_500)
product3 = Product("Велосипед", 8_300)

# Создаем клиентов
customer1 = Customer("Вася")
customer2 = Customer("Петя")
customer3 = Customer("Маша")

# Создаем скидки
discount1 = Discount("За красивые глаза", 30)
discount2 = Discount("За красоту и вдохновение", 10)
discount3 = Discount("Просто так", 5)

# Создаем заказы
order1 = Order([product1])
order2 = Order([product2, product1])
order3 = Order([product2, product3])

# Применяем скидки к заказам
order1.add_discount(discount1)
order1.add_discount(discount2)

order2.add_discount(discount2)
order2.add_discount(discount3)

order3.add_discount(discount2)

# Добавляем заказы клиентам
customer1.add_order(order1)
customer1.add_order(order2)

customer2.add_order(order2)
customer2.add_order(order3)

customer3.add_order(order3)

# Считаем общее количество заказов и общую сумму всех заказов для всех клиентов
print(f"Всего заказов: {Order.orders_count()} на сумму {Order.total_price_all()}")

# Выводим информацию о клиентах, заказах и продуктах с использованием дандер-методов
print()
print(f"Продукт 1: [{product1}]")
print(f"Продукт 2: [{product2}]")
print(f"Продукт 3: [{product3}]")

print()
print(f"Скидка 1: [{discount1}]")
print(f"Скидка 2: [{discount2}]")
print(f"Скидка 3: [{discount3}]")

print()
print(f"Заказ 1: [{order1}]")
print(f"Заказ 2: [{order2}]")
print(f"Заказ 3: [{order3}]")

print()
print(f"Клиент 1: [{customer1}]")
print(f"Клиент 2: [{customer2}]")
print(f"Клиент 3: [{customer3}]")


