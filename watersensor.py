#Libraries
import RPi.GPIO as GPIO
import time

watersensorpin =  14
GPIO_LED = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(watersensorpin, GPIO.IN)
GPIO.setup(GPIO_LED, GPIO.OUT)

while 1:
	if GPIO.input(watersensorpin):
	
		GPIO.output(GPIO_LED, 0)
		time.sleep(1)
	else:
		print("Water Detected!")
		GPIO.output(GPIO_LED, 1)
		time.sleep(1)

