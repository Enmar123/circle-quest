
import time
import math as m
import numpy as np


class World():

    def __init__(self):
        self.pitch = 0
        self.roll = 0
    def readFile(self):
        file = open("imu_data.txt","r")
        reading = file.readlines()
        self.pitch = reading[1]
	self.roll = reading[2]

if __name__=="__main__":
    
    world = World()
    
    while True:
        world.readFile()
        print(world.pitch)
        print(world.roll)
        print("")
        time.sleep(1)
        
    
    
