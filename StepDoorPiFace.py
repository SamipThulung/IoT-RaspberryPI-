from time import sleep
import pifacecad
import RPi.GPIO as GPIO 
GPIO.cleanup()
GPIO.setmode(GPIO.BCM) 
# PIN-Assignment 
A=12 
B=16
C=20 
D=21 
time = 0.001 

# defining the PINs 
GPIO.setup(A,GPIO.OUT) 
GPIO.setup(B,GPIO.OUT) 
GPIO.setup(C,GPIO.OUT) 
GPIO.setup(D,GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, True)
GPIO.output(A, False) 
GPIO.output(B, False) 
GPIO.output(C, False) 
GPIO.output(D, False) 

# driving the motor 
def Step1(): 
	GPIO.output(D, True) 
	sleep (time) 
	GPIO.output(D, False)

def Step2(): 
	GPIO.output(D, True) 
	GPIO.output(C, True) 
	sleep (time) 
	GPIO.output(D, False) 
	GPIO.output(C, False) 

def Step3(): 
	GPIO.output(C, True) 
	sleep (time) 
	GPIO.output(C, False)

def Step4(): 
	GPIO.output(B, True) 
	GPIO.output(C, True) 
	sleep (time) 
	GPIO.output(B, False) 
	GPIO.output(C, False) 

def Step5(): 
	GPIO.output(B, True) 
	sleep (time) 
	GPIO.output(B, False) 

def Step6(): 
	GPIO.output(A, True) 
	GPIO.output(B, True) 
	sleep (time) 
	GPIO.output(A, False) 
	GPIO.output(B, False) 

def Step7(): 
	GPIO.output(A, True) 
	sleep (time) 
	GPIO.output(A, False) 

def Step8(): 
	GPIO.output(D, True) 
	GPIO.output(A, True) 
	sleep (time) 
	GPIO.output(D, False) 
	GPIO.output(A, False)
cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
while True:
        GPIO.output(26, True)
        cad.lcd.blink_off()
        cad.lcd.cursor_off()
        cad.lcd.clear()
        cad.lcd.write("Enter Passcode: ")
        passcode=input("Enter Passcode: ")
        cad.lcd.set_cursor(0,1)
        cad.lcd.write("***")
        sleep(2)        
        #print (type(passcode))
        if passcode=='123':
                cad.lcd.clear()
                cad.lcd.write("Access Granted")
                sleep(2)
                cad.lcd.clear()
                cad.lcd.write("Door is opening.")
                cad.lcd.set_cursor(0,1)
                cad.lcd.write("Please! Wait")
                # start one complete turn 
                for i in range (512): 
                        Step8() 
                        Step7() 
                        Step6() 
                        Step5() 
                        Step4() 
                        Step3() 
                        Step2() 
                        Step1()
                sleep(7)
                cad.lcd.clear()
                cad.lcd.write("Door is closing.")
                sleep(1)
                for i in range(512):
                        Step1()
                        Step2()
                        Step3()
                        Step4()
                        Step5()
                        Step6()
                        Step7()
                        Step8()
        else:
                cad.lcd.clear()
                cad.lcd.write("Wrong passcode.")
                cad.lcd.set_cursor(0,1)
                cad.lcd.write("Access Denied!")
                sleep(7)
GPIO.cleanup()
GPIO.output(26, True)
