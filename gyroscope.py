#!/usr/bin/python3

from sense_hat import SenseHat
import time
sense = SenseHat()
while True:    
    orientation = sense.get_orientation_degrees()
    #raw = sense.get_accelerometer_raw()
    print("Pitch: {pitch}, Roll: {roll}, Yaw: {yaw}".format(**orientation))
    #print("X: {x}, Y: {y}, Z: {z}".format(**raw))
    time.sleep(1)


