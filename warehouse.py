import numpy


class WareHouse:
    def __init__(self, x, y, stock):
        self.x = x
        self.y = y
        self.stock = stock
        return

    def distance_to(self, target):
        if isinstance(target, WareHouse):
            return numpy.math.sqrt((int(self.x) - int(target.x)) ** 2 + (int(self.y) - int(target.y)) ** 2)
        else:
            raise ValueError('Target was not a warehouse instance')
