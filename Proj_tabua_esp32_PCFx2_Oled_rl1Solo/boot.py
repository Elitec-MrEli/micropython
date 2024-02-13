# Complete project details at https://RandomNerdTutorials.com
import socket
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
reb_ = machine.Pin(15, machine.Pin.OUT)

reb_.value(0) #começa com sistema ativado se desligar essa porta o esp desliga

ssid = 'elitec_testes'
password = '12345678'
mqtt_server = 'gerirsistemas.com.br'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'

client_id = b'ElitecPython:'+ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'hello'

last_message = 0
message_interval = 30
last_message_limp_t = 0
limp_t_interval = 10
counter = 0
tempo_antes_reiniciar_por_falha_mqtt = 60
bol_limp_t = True

linha1 = '*'
linha2 = '*'
linha3 = '*'
linha4 = '*'
ponteiro_linha = 0

import socket

def leia_pinos():
    global str_pcf1
    global str_pcf2
    #
    if len(str(converter(pcf.port,2)))   == 7:    
        str_pcf1 = "0"+str(converter(pcf.port,2))      
    elif len(str(converter(pcf.port,2))) == 6:
        str_pcf1 = "00"+str(converter(pcf.port,2))
    elif len(str(converter(pcf.port,2))) == 5:
        str_pcf1 = "000"+str(converter(pcf.port,2))
    elif len(str(converter(pcf.port,2))) == 4:
        str_pcf1 = "0000"+str(converter(pcf.port,2))
    elif len(str(converter(pcf.port,2))) == 3:
        str_pcf1 = "00000"+str(converter(pcf.port,2))
    elif len(str(converter(pcf.port,2))) == 2:
        str_pcf1 = "000000"+str(converter(pcf.port,2))
    elif len(str(converter(pcf.port,2))) == 1:
        str_pcf1 = "0000000"+str(converter(pcf.port,2))
    elif len(str(converter(pcf.port,2))) == 0:
        str_pcf1 = "00000000"+str(converter(pcf.port,2))    
    else:
        str_pcf1 = str(converter(pcf.port,2))
    #
    if len(str(converter(pcf2.port,2)))   == 7:    
        str_pcf2 = "0"+str(converter(pcf2.port,2))      
    elif len(str(converter(pcf2.port,2))) == 6:
        str_pcf2 = "00"+str(converter(pcf2.port,2))
    elif len(str(converter(pcf2.port,2))) == 5:
        str_pcf2 = "000"+str(converter(pcf2.port,2))
    elif len(str(converter(pcf2.port,2))) == 4:
        str_pcf2 = "0000"+str(converter(pcf2.port,2))
    elif len(str(converter(pcf2.port,2))) == 3:
        str_pcf2 = "00000"+str(converter(pcf2.port,2))
    elif len(str(converter(pcf2.port,2))) == 2:
        str_pcf2 = "000000"+str(converter(pcf2.port,2))
    elif len(str(converter(pcf2.port,2))) == 1:
        str_pcf2 = "0000000"+str(converter(pcf2.port,2))
    elif len(str(converter(pcf2.port,2))) == 0:
        str_pcf2 = "00000000"+str(converter(pcf2.port,2))    
    else:
        str_pcf2 = str(converter(pcf2.port,2))

def imprime_oled(txt):
    global linha1, linha2, linha3, linha4, ponteiro_linha    
    limpa_t()    
    if ponteiro_linha == 0:
        oled.text(txt, 0, ponteiro_linha)
        ponteiro_linha = ponteiro_linha + 9
        linha1 = txt
    elif ponteiro_linha == 9:        
        oled.text(txt, 0, ponteiro_linha)
        ponteiro_linha = ponteiro_linha + 9
        linha2 = txt
        oled.text(linha1, 0, 0)
    elif ponteiro_linha == 18:
        oled.text(txt, 0, ponteiro_linha-3)
        ponteiro_linha = ponteiro_linha + 9
        linha3 = txt
        oled.text(linha1, 0, -3)
        oled.text(linha2, 0, 6)
    elif ponteiro_linha == 27:
        oled.text(txt, 0, ponteiro_linha -3)
        ponteiro_linha = ponteiro_linha +9
        linha4 = txt
        oled.text(linha1, 0, -3)
        oled.text(linha2, 0, 6)
        oled.text(linha3, 0, 15) 
    else:
        linha1 = linha2
        linha2 = linha3
        linha3 = linha4 
        linha4 = txt
        oled.text(linha1, 0, -3)
        oled.text(linha2, 0, 6)
        oled.text(linha3, 0, 15)
        oled.text(linha4, 0, 24)     
    oled.show()    

def http_get(url): # essa função pega uma pagina web, PARA USO FUTURO
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host),'utf8'))
    while True:
      data = s.recv(100)
      if data:
          print(str(data, 'utf8'), end='')
      else:
          break
    s.close()
    
#def tente_conectar_wifi():
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)


#print('REDES AO ALCANÇE DO ESP:')
#print(station.scan())

#tente_conectar_wifi()

"""
# O COD ABAIXO NO DIA 13/02/2024 GERA UM ERRO QUE PARECE ESTAR RELACIONANDO AO FIRM PYTHON
#             wifi:sta is connecting, return error
#          Traceback (most recent call last):
while station.isconnected() == False:
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    print(station.isconnected())
    print('falha na conecção wifi reboot em --10--')
    time.sleep(10)        
    #tente_conectar_wifi()
    print('reboot__ando...')    
    machine.reset()
"""  

if station.isconnected() == False:
    print('Falha ao conectar ao WIFI')    
    print('REDES AO ALCANÇE DO ESP:')
    print(station.scan())
    
else:
    print('Conectado com SUCESSO ip:')
    print(station.ifconfig())