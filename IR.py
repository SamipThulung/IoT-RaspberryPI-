import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(2,IO.OUT) #GPIO 2 -> Red LED as output
IO.setup(23,IO.OUT) #GPIO 23 -> Green LED as output
IO.setup(25,IO.IN) #GPIO 25 -> IR sensor as input
while 1:
    if(IO.input(25)==True): #object is far away
        print ("object is far away")
        IO.output(23,False) #Red led ON
        IO.output(2,True) # Green led OFF
    
    if(IO.input(25)==False): #object is near
        print ("object is near ")
        IO.output(23,True) #Green led ON
        IO.output(2,False) # Red led OFF