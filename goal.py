import numpy as np

class Goal():
    def __init__(self):
        self.pos = 0
        self.width = 2
        self.r = 0
        self.g = 100
        self.b = 50
        self.w = 0
        self.flash_state = True
        self.danger = False
        self.goal = True

    def update_flash(self):
        if self.flash_state:
            self.flash_state = False
            self.g = 200
            self.r = 40
        if not self.flash_state:
            self.flash_state = True
            self.g = 0
            self.r = 200
        print(self.flash_state)
        
    def rgb_out(self):
        return np.array([[self.r, self.g, self.b, self.w]]*self.width)
        

