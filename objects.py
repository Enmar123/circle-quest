import numpy as np

class Goal():
    def __init__(self):
        self.loc = 0
        self.width = 0
        self.r = 0
        self.g = 255
        self.b = 50
        self.w = 255
        self.flash_state = True

    def update_flash(self):
        if self.flash_state = True:
            self.flash_state = False
