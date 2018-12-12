import numpy

from warehouse import WareHouse
from order import Order


def main():
    filename = 'busy_day.in'
    orders, warehouses = import_txt(filename)
    q1 = total_stocks(orders=orders, warehouses=warehouses)
    q2 = max_weight(orders)
    q3 = max_distance(warehouses)
    export_txt('busy_day.out', q1, q2, q3)
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
        order = Order(int(cords[0]), int(cords[1]), prod, C_a)
        orders.append(order)
    return orders, warehouses


def export_txt(file, q1, q2, q3):
    out = open(file, 'w')
    out.write('Google hashcode 2016 | Delivery | Inputfile: {} \n\n'.format(file))
    out.write('1. Totale resterende stock berekenen van alle magazijnen samen nadat alle orders uitgevoerd zijn. M.a.w.: wat ligt er nog in de magazijnen nadat alle bestellingen geleverd zijn? \n')
    out.write('De totale stock: {} \n\n'.format(q1))
    out.write('2. Welke order(s) weegt/wegen het zwaarst? Hoe zwaar weegt deze order? \n')
    out.write('Dit product weegt het zwaarst: {}\n\n'.format(q2))
    out.write('3. Welke 2 magazijnen liggen het verst uit elkaar? \n')
    out.write('De coordinaten zijn: ({}, {}) en ({}, {})\n'.format(q3[0].x, q3[0].y, q3[1].x, q3[1].y))



def total_stocks(orders, warehouses):
    stocks = [0] * len(warehouses[0].stock)
    for warehouse in warehouses:
        stocks = [a + b for a, b in zip(warehouse.stock, stocks)]
    for order in orders:
        stocks = [a - b for a, b in zip(stocks, order.bought)]
    return stocks


def max_weight(orders):
    return max([order.totalweight for order in orders])


def max_distance(warehouses):
    wh1 = None
    wh2 = None
    max_dist = 0
    for j in warehouses:
        for k in warehouses:
            t = j.distance_to(k)
            if t > max_dist:
                max_dist = t
                wh1 = j
                wh2 = k
    return wh1, wh2


if __name__ == '__main__':
    main()

