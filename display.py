
from machine import Pin, I2C
import ssd1306
import time
from time import sleep
import pcf8574
from pcf8574 import*
from machine import I2C, Pin


i2c = I2C(0, scl=Pin(22), sda=Pin(21),freq=100000)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

def limpa_t():
    oled.fill_rect(0, 0, 128, 32 , 0)
    oled.show()

def inicializacao():
    #--------------------------------------------    
    oled.text('----------------', 0, 0)
    oled.text('Elitec Sistemas', 0, 9)
    oled.text('Seja Bem Vindo..', 0, 19)
    oled.text('----------------', 0, 28)
    oled.show()
    time.sleep(0.2)
    limpa_t()
    oled.invert(1)
    oled.text('----------------', 0, 0)
    oled.text('Elitec Sistemas', 0, 9)
    oled.text('Seja Bem Vindo..', 0, 19)
    oled.text('----------------', 0, 28)
    oled.show()
    time.sleep(0.2)
    oled.invert(0)
    limpa_t()
    oled.text('----------------', 0, 0)
    oled.text('Elitec Sistemas', 0, 9)
    oled.text('Seja Bem Vindo..', 0, 19)
    oled.text('----------------', 0, 28)
    oled.show()
    time.sleep(0.2)
    limpa_t()
    oled.invert(1)
    oled.text('----------------', 0, 0)
    oled.text('Elitec Sistemas', 0, 9)
    oled.text('Seja Bem Vindo..', 0, 19)
    oled.text('----------------', 0, 28)
    oled.show()
    time.sleep(0.2)
    oled.invert(0)
    limpa_t()
    #--------------------------------------------

#inicializacao()

"""
oled.invert(1)
oled.fill(0)
oled.fill_rect(0, 0, 32, 32, 1)
oled.fill_rect(2, 2, 28, 28, 0)
oled.vline(9, 8, 22, 1)
oled.vline(16, 2, 22, 1)
oled.vline(23, 8, 22, 1)
oled.fill_rect(26, 24, 2, 4, 1)
oled.text('MicroPython', 40, 0, 1)
oled.text('SSD1306', 40, 12, 1)
oled.text('OLED 128x64', 40, 24, 1)
oled.show()
"""

