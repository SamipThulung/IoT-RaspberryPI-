#!/usr/bin/python3
import pifacecad
import time
cad = pifacecad.PiFaceCAD() 	# Create PiFace Control and Display Object
cad.lcd.backlight_on()
cad.lcd.write("Hello, World")
time.sleep(2)
cad.lcd.clear()
cad.lcd.write("Click the button")
while True:
    if(cad.switches[0].value == 1):
        cad.lcd.clear()
        cad.lcd.write("Btn1 is pressed")
        time.sleep(2)
        cad.lcd.clear()
        cad.lcd.write("Click the button")
    if(cad.switches[1].value == 1):
        cad.lcd.clear()
        cad.lcd.write("Btn2 is pressed")
        time.sleep(2)
        cad.lcd.clear()
        cad.lcd.write("Click the button")
    if(cad.switches[2].value == 1):
        cad.lcd.clear()
        cad.lcd.write("Btn3 is pressed")
        time.sleep(2)
        cad.lcd.clear()
        cad.lcd.write("Click the button")
    if(cad.switches[3].value == 1):
        cad.lcd.clear()
        cad.lcd.write("Btn4 is pressed")
        time.sleep(2)
        cad.lcd.clear()
        cad.lcd.write("Click the button")
    if(cad.switches[4].value == 1):
        cad.lcd.clear()
        cad.lcd.write("Exiting...")
        time.sleep(2)
        cad.lcd.clear()
        cad.lcd.backlight_off()
        cad.lcd.blink_off()
        break