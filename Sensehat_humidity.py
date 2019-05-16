#Islington College


from sense_hat import SenseHat #Calling Header file for SenseHat

sense = SenseHat()

green = (0, 255, 0) #Set Color to Green
white = (255, 255, 255) #set color for white

while True:
    humidity = sense.humidity #call humidity from sensehat
    humidity_value = 64 * humidity / 100 #Formula calculating humidity
    print(humidity) #Print humidity in console

    pixels = [green if i < humidity_value else white for i in range(64)]

    sense.set_pixels(pixels) # Print humidity in sensehat led