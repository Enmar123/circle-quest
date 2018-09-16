
import time
import math as m
import numpy as np


class World():

    def __init__(self):
        self.pitch = 0
        self.roll = 0
    def readFile(self):
        file = open("imu_data.txt","r")
        self.pitch = file.readline(2)
        self.roll = file.readline(3)

if __name__=="__main__":
    
    world = World()
    
    while True:
        world.readFile()
        print("pitch =", world.pitch)
        print("roll =", world.roll)
        print("")
        time.sleep(1)
        
    
    