import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_LED = 23
pirsensor =  15
GPIO.setup(pirsensor, GPIO.IN)
GPIO.setup(GPIO_LED, GPIO.OUT)
time.sleep(2)
GPIO.output(GPIO_LED, 1)

while 1:
	if GPIO.input(pirsensor):
		print("Motion Detected!")
		GPIO.output(GPIO_LED, 1)
		time.sleep(2)
	else:
            print ('motion not detected')
            GPIO.output(GPIO_LED, 0)
	time.sleep(0.1)
GPIO.cleanup()

