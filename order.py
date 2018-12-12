class Order:
    def __init__(self, x, y, bought, weight):
        self.bought = bought
        self.weights = weight
        self.x = x
        self.y = y
        self.totalweight = self.total_weight()
    pass

    def total_weight(self):
        return sum([int(a) * b for a, b in zip(self.weights, self.bought)])


