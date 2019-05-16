#Islington College


from sense_hat import SenseHat #Import Sensehat library

sense = SenseHat() #declare sense 

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp = sense.temp #Call for temp module
    print(temp) #console print temp

    pixels = [red if i < temp else blue for i in range(64)]

    sense.set_pixels(pixels) #LED print temp