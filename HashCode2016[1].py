import numpy


def main():
    filename = 'busy_day.in'
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
        warehouse = {'x': int(cords[0]), 'y': int(cords[1]), 'stock': stock}
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
        order = {'x': int(cords[0]), 'y': int(cords[1]), 'bought': prod, 'items': items}
        orders.append(order)
    stocks = [0] * P
    for stock in warehouses:
        stocks = [x + y for x, y in zip(stock['stock'], stocks)]
    print(stocks)
    for bought in orders:
        stocks = [x - y for x, y in zip(stocks, bought['bought'])]
    print(stocks)
    sums = []
    for ord in orders:
        sums.append(sum([int(x) * y for x, y in zip(C_a, ord['bought'])]))
    print(sums)
    print(max(sums))
    print(numpy.argmax(sums))
    b = 0
    a = None
    c = None
    for w_b in warehouses:
        for w_a in warehouses:
            dis = distance(w_a, w_b)
            print(dis)
            if dis > b:
                b = dis
                a = w_a
                c = w_b
    print(b)
    print(a)
    print(c)
    outfile = filename.replace('.in', '.out')
    out = open(outfile, 'w')
    out.write('Google hashcode 2016 | Delivery | Inputfile: {} \n\n'.format(filename))
    out.write('1. Totale resterende stock berekenen van alle magazijnen samen nadat alle orders uitgevoerd zijn. M.a.w.: wat ligt er nog in de magazijnen nadat alle bestellingen geleverd zijn? \n')
    out.write('De totale stock: {} \n\n'.format(stocks))
    out.write('2. Welke order(s) weegt/wegen het zwaarst? Hoe zwaar weegt deze order? \n')
    out.write('Dit product weegt het zwaarst: {} met het ID: {}\n\n'.format(max(sums), numpy.argmax(sums)))
    out.write('3. Welke 2 magazijnen liggen het verst uit elkaar? \n')
    out.write('De maximale afstand is: {}. coordinaten zijn: ({}, {}) en ({}, {})\n'.format(b, a['x'], a['y'], c['x'], c['y']))


def distance_a(a, b):
    """
    can't return negative numbers!
    """
    if b['x'] > a['x']:
        result = {'distance_x': b['x'] - a['x'], 'distance_y': b['y'] - a['y']}
        return result
    else:
        result = {'distance_x': a['x'] - b['x'], 'distance_y': a['y'] - b['y']}
        return result


def distance_b(a, b):
    """
    can return negative numbers!
    """
    result = {'distance_x': b['x'] - a['x'], 'distance_y': b['y'] - a['y']}
    return result


def distance(a, b):
    # value = numpy.math.sqrt(a * a + b * b)
    a_x = a['x']
    a_y = a['y']
    b_x = b['x']
    b_y = b['y']
    # value = numpy.math.sqrt(a_y * a_x + b_y * b_x)
    value = numpy.math.sqrt((b_x-a_x) ** 2 + (b_y-a_y) ** 2)
    return value


if __name__ == '__main__':
    main()