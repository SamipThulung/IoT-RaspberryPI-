import RPi.GPIO as Blink_led
import time
Blink_led.setmode(Blink_led.BCM)
Blink_led.setup(23, Blink_led.OUT)
for counter in range(0,10000):
    Blink_led.output(23,True)
    time.sleep(1)
    Blink_led.output(23,False)
    time.sleep(1)
Blink_led.output(False)