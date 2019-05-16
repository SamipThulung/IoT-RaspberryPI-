#Libraries
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO_LED = 23

GPIO.setup(GPIO_LED, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_LED, 0)
def distance():
	GPIO.output(GPIO_TRIGGER, True)

	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	StartTime = time.time()
	StopTime = time.time()

	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()

	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()

	TimeElapsed = StopTime - StartTime

	distance = (TimeElapsed * 34000) / 2
	return distance

if __name__ == '__main__':
	try:
		while True:
			dist = distance()
			if (dist <= 150):
				GPIO.output(GPIO_LED, 1)
				print("The Measured Distance is: %.2fcm" % dist)
				time.sleep(1)
			else:
				GPIO.output(GPIO_LED, 0)
	except KeyboardInterrupt:
		print("Measurement Has stopped by user!!")
		GPIO.cleanup()
