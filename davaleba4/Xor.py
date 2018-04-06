import numpy as np


class Xor:
    def __init__(self, x1, x2):
        self.T = 0
        self.w = [1, 1]
        self.y = self.datvale_y(x1, x2)

    def datvale_y(self, x1, x2):
        return self.f(np.sum(np.multiply(self.w, [x1, x2])) - self.T)

    def f(self, a):
        if a > 0:
            return 1
        return 0
