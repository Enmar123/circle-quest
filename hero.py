import numpy as np

class Hero():
    def __init__(self):
        self.pos = 0
        self.r = 0
        self.g = 0
        self.b = 40
        self.w = 100
        self.vel = 0
        self.dead = False

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
            self.b = 0
            self.dead = True
            
    def move(self):
        self.loc += self.vel
        self.loc = self.loc%35

    def resurrect(self):
        self.w = 255
        self.b = 40
        self.dead = False
        
    def ckeck(self, obj):
        if self.pos == obj.pos and obj.danger == True:
            self.dead = True
            self.vel = 0
    
                
            
        
        
