
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
        pitch = reading[1]
        roll = reading[2]
        file.close()
    
        self.pitch = float(pitch.strip('pitch: '))
        self.roll = float(roll.strip('roll: '))

if __name__=="__main__":
    
    world = World()
    
    while True:
        world.readFile()
        print(world.pitch)
        print(world.roll)
        print("")
        time.sleep(1)
        
    
    
