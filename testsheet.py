#!/usr/bin/python3
"""
Created on Tue Jul  3 19:09:50 2018


"""
import sheetupdate
import datetime
from  random import randint
from time import sleep
from sense_hat import SenseHat

def testsheet():
    spreadsheetId = '1ghfoefFm1j4h9FyGuW1VLXyxaYjiGGBDftaqK7EjpkQ'
    #spreadsheetId = '1xUDzb7SC42LO_mpHyxepDkZoTJNjjBrqAWAvwcaFsp8'
    rangeName = 'A1:D'
    values = {"values":[["Time","Temp(C)","Pressure(mmHg)","Humidity(%)"],]}
    
    sheetupdate.update_authenticate(spreadsheetId, rangeName, values)
    sense = SenseHat()
    try:
        while True:
            for i in range(2,999):
                myTS = "{:%H:%M:%S}".format(datetime.datetime.now())
                t = round(sense.get_temperature(),2)
                p = round(sense.get_pressure(),2)
                h = round(sense.get_humidity(),2)
                values = {"values":[[myTS,t, p, h],]}
                rangeName = 'A' + str(i) + ':D'
                sheetupdate.update_authenticate(spreadsheetId, rangeName, values)
                sleep(11)
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    testsheet()
        

