# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 00:37:19 2018

@author: Jason
"""

from imu import imu_data_callback
import sleep


while True:
    imu_data_callback()
    sleep(1)