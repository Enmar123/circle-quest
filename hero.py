import numpy as np

class Hero():
    def __init__(self):
        self.loc = 0
        self.r = 0
        self.g = 0
        self.b = 0
        self.w = 255
        self.vel = 0

    def rgb_out(self):
        return np.array([self.r, self.g, self.b, self.w])

    def dead(self):
        self.w = 0

    def get_health(self, amt):
        self.w += amt
        if self.w >= 255:
            self.w = 255

    def lose_health(self, amt):
        self.w -= amt
        if self.w <= 0:
            self.w = 0
        
    def move(self):
        self.loc += int(self.vel)
