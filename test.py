# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 00:37:19 2018

@author: Jason
"""
from matrix_io.proto.malos.v1 import driver_pb2 # MATRIX Protocol Buffer driver library
from matrix_io.proto.malos.v1 import sense_pb2 # MATRIX Protocol Buffer sensor library
from imu import imu_data_callback
from time import sleep


while True:
    data = sense_pb2.Imu().FromString(data[0])
    print(imu_data_callback(data))
    sleep(1)