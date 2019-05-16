#!/usr/bin/python3

from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()
temp = sense.get_temperature()
pressure = sense.get_pressure()

print("Humidity: %s %%rH" % int(humidity))
print("Temperature: %s C" % int(temp))
print("Pressure: %s Millibars" % int(pressure))
