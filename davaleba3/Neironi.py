import numpy as np


class Neironi:
    def __init__(self, T, w):
        self.T = T
        self.w = w
        self.y = 0

    def datvale_y(self, x):
        self.y = self.f(np.sum(np.multiply(x, self.w)) - self.T)

    def f(self, a):
        return 1/(1+np.exp(-a))
