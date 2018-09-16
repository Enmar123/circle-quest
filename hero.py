import numpy as np
import math as m

class Hero():
    def __init__(self, spawn):
        self.spawn = spawn
        self.pos = spawn
        self.r = 0
        self.g = 0
        self.b = 40
        self.w = 100
        self.vel = 0
        self.count = 0
        self.dead = False
        self.won = False

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
        self.pos += self.vel
        self.pos = self.pos%35

    def resurrect(self):
        self.w = 255
        self.b = 40
        self.dead = False
        self.won = False
        self.pos = self.spawn
        
    def check(self, obj):
        if self.pos == obj.pos and obj.danger == True:
            self.dead = True
            
        if self.pos == obj.pos and obj.goal == True:
            self.won = True
            
    
    def speed(self, pitch, roll):
        
        self.vel = m.hypot(pitch, roll)
        
        theta = np.arctan2(pitch, roll)
        inc = 2*m.pi/35
        led = int(theta/inc)
    
        for i in range(int(35/2)):
            loc = (led - i)%35
            if loc == self.pos :
                self.vel = self.vel * -1
                
        for i in range(int(35/2)):
            loc = (led - i)%35
            if loc == self.pos :
                self.vel = self.vel * 1
                
    def blink(self):
        if self.count < 10:
            if self.count % 2 == 0:
                self.w = 100 
            else:
                self.w = 0
                
            self.count = self.count + 1
        else:
            self.count = 0
            self.resurrect
            

        
        
