import numpy as np
from random import randint

class Lava():
    def __init__(self):
        self.pos = 0
        self.r = 100
        self.g = 0
        self.b = 0
        self.w = 0
        self.danger = True
        self.goal = False
        self.count = 0

    def rgb_out(self):
        return np.array([self.r, self.g, self.b, self.w])

    def pulse(self):
        limit = randint(10, 20)
        self.count= self.count + 1
        self.count = self.count%limit
        if self.count < limit/2:
            self.r = 100
            self.danger = True
        else:
            self.r = 0
            self.danger = False

        
