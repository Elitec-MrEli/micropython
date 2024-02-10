# Complete project details at https://RandomNerdTutorials.com
import time
from time import sleep # Get the sleep library from the time module.
from umqttsimple import MQTTClient
import ubinascii
import machine
from machine import Pin # Get the Pin function from the machine module.
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

led = machine.Pin(2, machine.Pin.OUT)

ssid = 'elitec_testes_off'
password = '12345678'
mqtt_server = 'gerirsistemas.com.br'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'hello'

last_message = 0
message_interval = 30
last_message_limp_t = 0
limp_t_interval = 10
counter = 0
tempo_antes_reiniciar_por_falha_mqtt = 60
bol_limp_t = True

linha1,linha2,linha3,linha4 = ' '


station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())