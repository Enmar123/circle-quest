import numpy as np

class ImageCreator():
    def __init__(self):
        self.led_count = 35
        self.out = np.zeros([35,4]) 

    def set_led(self, index, r,g,b,w):
        self.out[index] = [r,g,b,w]

    def clear_led(self, index):
        self.out[index] = [0,0,0,0]

    def brighten_led(self, index, intensity):
        img.out[2][img.out[2] >0 ] += intensity 

    def dim_led(self, index, intensity):
        img.out[2][img.out[2] >0 ] -= intensity 
        

