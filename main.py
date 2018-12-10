import numpy

from warehouse import WareHouse
from order import Order


def main():
    filename = 'busy_day.in'
    orders, warehouses = import_txt(filename)
    print(total_stocks(orders=orders, warehouses=warehouses))
    print(orders[0].bought)
    max_distance(warehouses)
    return


def import_txt(filename):
    file = open(filename)
    line = file.readline().strip().split(' ')
    R = int(line[0])
    C = int(line[1])
    D = int(line[2])
    T = int(line[3])
    W_max = int(line[4])
    P = int(file.readline().strip())
    C_a = file.readline().strip().split(' ')
    L = int(file.readline().strip())
    warehouses = []
    for _ in range(L):
        cords = file.readline().strip().split(' ')
        stock = file.readline().strip().split(' ')
        stock = [int(x) for x in stock]
        warehouse = WareHouse(cords[0], cords[1], stock)
        warehouses.append(warehouse)
    N = file.readline().strip()
    orders = []
    for _ in range(int(N)):
        cords = file.readline().strip().split(' ')
        items = int(file.readline().strip())
        deli = file.readline().strip().split(' ')
        prod = [0] * P
        for item in deli:
            prod[int(item)] += 1
        # order = {'x': int(cords[0]), 'y': int(cords[1]), 'bought': prod, 'items': items}
        order = Order(int(cords[0]), int(cords[1]), prod, items)
        orders.append(order)
    return orders, warehouses


def total_stocks(orders, warehouses):
    stocks = [0] * len(warehouses[0].stock)
    for warehouse in warehouses:
        stocks = [a + b for a, b in zip(warehouse.stock, stocks)]
    for order in orders:
        stocks = [a - b for a, b in zip(stocks, order.bought)]
    return stocks


def max_weight(orders):
    return max(order.totalweight for order in orders)


def max_distance(warehouses):
    for j in warehouses:
        for k in warehouses:
            print(j.distance_to(k))


if __name__ == '__main__':
    main()

