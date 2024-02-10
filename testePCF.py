import pcf8574
from machine import I2C, Pin
import time
from time import sleep # Get the sleep library from the time module.



"""
#(ESP32)
i2c = I2C(scl=Pin(22), sda=Pin(21))
pcf = pcf8574.PCF8574(i2c, 33)
pcf2 = pcf8574.PCF8574(i2c, 32)

pcf.pin(0, 0)
pcf.pin(1, 0)
pcf.pin(2, 0)
pcf.pin(3, 0)
pcf.pin(4, 1)
pcf.pin(5, 1)
pcf.pin(6, 1)
pcf.pin(7, 1)

pcf2.pin(0, 1)
pcf2.pin(1, 1)
pcf2.pin(2, 1)
pcf2.pin(3, 1)
pcf2.pin(4, 0)
pcf2.pin(5, 0)
pcf2.pin(6, 0)
pcf2.pin(7, 0)

time.sleep(5)
pcf.port = 0xff
pcf2.port = 0xff
"""


"""
# read pin 2
pcf.pin(2)

# set pin 3 HIGH
pcf.pin(3, 1)

# set pin 4 LOW
pcf.pin(4, 0)

# toggle pin 5
pcf.toggle(5)

# set all pins at once with 8-bit int
pcf.port = 0xff

# read all pins at once as 8-bit int
pcf.port
"""