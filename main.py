
import display
from display import*
import pcf8574
from machine import I2C, Pin

# TinyPICO (ESP32)
#i2c = I2C(scl=Pin(22), sda=Pin(21))
pcf = pcf8574.PCF8574(i2c, 33)
pcf2 = pcf8574.PCF8574(i2c, 32)

# "converte" n para uma outra base
def converter(n, base):
    if base == 10: # se for base 10, retorna o próprio número
        return n

    result = expoente = 0
    while n > 0:
        n, digito = divmod(n, base)
        result += (10 ** expoente) * digito
        expoente += 1        
    
    return result

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'reboot':
    print('REBOOT recebido executando em...')
    print('--5--')
    time.sleep(1)
    print('--4--')
    time.sleep(1)
    print('--3--')
    time.sleep(1)
    print('--2--')
    time.sleep(1)
    print('--1--')
    time.sleep(1)
    print('reboot__ando...')
    machine.reset()
#---------------------------------    
  global state 
  if msg == b"1":        
        if str(led.value()) == "1":
            print('led ja ligado')
        else:
            msg = b'Confirmando... ligando led'
            client.publish(topic_pub, msg)
            print('ligando led')
            limpa_t()
            display.oled.text('---------------', 0, 0)
            display.oled.text('led Lig =L', 0, 10)
            display.oled.text('---------------', 0, 20)
            display.oled.show()
            #bol_limp_t = True
            led.value(1)
            state = 0
  elif msg == b"0":                
        if str(led.value()) == "0":
            print('led ja desligado')
        else:
            msg = b'Confirmando... desligando led'
            client.publish(topic_pub, msg)
            print('deligando led')
            limpa_t()
            display.oled.text('---------------', 0, 0)
            display.oled.text('led Desl =D', 0, 10)
            display.oled.text('---------------', 0, 20)
            display.oled.show()
            #bol_limp_t = True
            led.value(0)
            state = 1
  elif msg == b"i":        
        # LED is inversed, so setting it to current state
        # value will make it 'i'
        state = str(led.value())
        #print(state)
        if state == "1":
            msg = b'Confirmando... invertendo led para desligado'
            client.publish(topic_pub, msg)
            led.value(0)
            state = 1
            print('invertendo led para desligado')
            limpa_t()
            display.oled.text('---------------', 0, 0)
            display.oled.text('led invert =D', 0, 10)
            display.oled.text('---------------', 0, 20)
            display.oled.show()
            #bol_limp_t = True
        elif state == "0":
            msg = b'Confirmando... invertendo led para ligado'
            client.publish(topic_pub, msg)
            led.value(1)
            state = 0
            print('invertendo led para ligado')
            limpa_t()
            display.oled.text('---------------', 0, 0)
            display.oled.text('led invert =L', 0, 10)
            display.oled.text('---------------', 0, 20)
            display.oled.show()
            #bol_limp_t = True
  elif msg == b"p101":
      pcf.pin(0, 0)
  elif msg == b"p100":    
      pcf.pin(0, 1)
  elif msg == b"p111":
      pcf.pin(1, 0)
  elif msg == b"p110":    
      pcf.pin(1, 1)
  elif msg == b"p121":
      pcf.pin(2, 0)
  elif msg == b"p120":    
      pcf.pin(2, 1)
  elif msg == b"p131":
      pcf.pin(3, 0)
  elif msg == b"p130":    
      pcf.pin(3, 1)
  elif msg == b"p141":
      pcf.pin(4, 0)
  elif msg == b"p140":    
      pcf.pin(4, 1)
  elif msg == b"p151":
      pcf.pin(5, 0)
  elif msg == b"p150":    
      pcf.pin(5, 1)
  elif msg == b"p161":
      pcf.pin(6, 0)
  elif msg == b"p160":    
      pcf.pin(6, 1)
  elif msg == b"p171":
      pcf.pin(7, 0)
  elif msg == b"p170":    
      pcf.pin(7, 1)
      
  elif msg == b"p201":
      pcf2.pin(0, 0)
  elif msg == b"p200":    
      pcf2.pin(0, 1)
  elif msg == b"p211":
      pcf2.pin(1, 0)
  elif msg == b"p210":    
      pcf2.pin(1, 1)
  elif msg == b"p221":
      pcf2.pin(2, 0)
  elif msg == b"p220":    
      pcf2.pin(2, 1)
  elif msg == b"p231":
      pcf2.pin(3, 0)
  elif msg == b"p230":    
      pcf2.pin(3, 1)
  elif msg == b"p241":
      pcf2.pin(4, 0)
  elif msg == b"p240":    
      pcf2.pin(4, 1)
  elif msg == b"p251":
      pcf2.pin(5, 0)
  elif msg == b"p250":    
      pcf2.pin(5, 1)
  elif msg == b"p261":
      pcf2.pin(6, 0)
  elif msg == b"p260":    
      pcf2.pin(6, 1)
  elif msg == b"p271":
      pcf2.pin(7, 0)
  elif msg == b"p270":    
      pcf2.pin(7, 1)
  elif msg == b"ptof":    
      pcf.port = 0xff
      pcf2.port = 0xff
  elif msg == b"pton":    
      pcf.port = 0
      pcf2.port = 0
  elif msg == b"p1t3":    
      pcf.pin(3, 0)
      print('pulso de 3 seg pcf1 porta 3')
      time.sleep(1)
      print('.')
      time.sleep(1)
      print('.')
      time.sleep(1)
      print('.')
      pcf.pin(3, 1)
  elif msg == b"p2t3":    
      pcf2.pin(3, 0)
      print('pulso de 3 seg pcf2 porta 3')
      time.sleep(1)
      print('.')
      time.sleep(1)
      print('.')
      time.sleep(1)
      print('.')
      pcf2.pin(3, 1)
#---------------------------------          
      
def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Conectado no MQTT %s, INSCRITO no TOPICO %s PUBLICANDO no TOPICO %s' % (mqtt_server, topic_sub, topic_pub))
  return client

def restart_and_reconnect(): # AQUI PARECE QUE O WHILE TRUE: FAZ UMATIVA DE PUB E SUB, COSO TIVER ERROS EXECUTA ESTA FUNÇÃO QUE COMUNICA FALHA E REBOOTA
  print('FALHA AO CONECTAR AO SERVER MQTT "'+ str(mqtt_server) +'" Reconectarei em...'+str(tempo_antes_reiniciar_por_falha_mqtt)+'Seg')
  time.sleep(1)
  global t_
  t_ = tempo_antes_reiniciar_por_falha_mqtt - 1  
  for numero in range(t_):    
        print(numero - t_)
        time.sleep(1) # AGUARDA '60' SEGUNDOS E REINICIA  
  machine.reset() # REINICIA O ESP...

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

inicializacao() #4 SEG DE ELITEC

global str_pcf1
global str_pcf2

if len(str(converter(pcf.port,2))) == 7:    
    str_pcf1 = "0"+str(converter(pcf.port,2))      
elif len(str(converter(pcf.port,2))) == 6:
    str_pcf1 = "00"+str(converter(pcf.port,2))
elif len(str(converter(pcf.port,2))) == 5:
    str_pcf1 = "000"+str(converter(pcf.port,2))
else:
    str_pcf1 = str(converter(pcf.port,2))

if len(str(converter(pcf2.port,2))) == 7:    
    str_pcf2 = "0"+str(converter(pcf2.port,2))      
elif len(str(converter(pcf2.port,2))) == 6:
    str_pcf2 = "00"+str(converter(pcf2.port,2))
elif len(str(converter(pcf2.port,2))) == 5:
    str_pcf2 = "000"+str(converter(pcf2.port,2))
else:
    str_pcf2 = str(converter(pcf2.port,2))

print('PCF1:|'+str_pcf1[0]+'-'+str_pcf1[1]+'-'+str_pcf1[2]+'-'+str_pcf1[3]+'-'+str_pcf1[4]+'-'+str_pcf1[5]+'-'+str_pcf1[6]+'-'+str_pcf1[7]+'|')
pcf.pin(7, int(str_pcf1[0]))
pcf.pin(6, int(str_pcf1[1]))
pcf.pin(5, int(str_pcf1[2]))
pcf.pin(4, int(str_pcf1[3]))
pcf.pin(3, int(str_pcf1[4]))
pcf.pin(2, int(str_pcf1[5]))
pcf.pin(1, int(str_pcf1[6]))
pcf.pin(0, int(str_pcf1[7]))

print('PCF2:|'+str_pcf2[0]+'-'+str_pcf2[1]+'-'+str_pcf2[2]+'-'+str_pcf2[3]+'-'+str_pcf2[4]+'-'+str_pcf2[5]+'-'+str_pcf2[6]+'-'+str_pcf2[7]+'|')
pcf2.pin(7, int(str_pcf2[0]))
pcf2.pin(6, int(str_pcf2[1]))
pcf2.pin(5, int(str_pcf2[2]))
pcf2.pin(4, int(str_pcf2[3]))
pcf2.pin(3, int(str_pcf2[4]))
pcf2.pin(2, int(str_pcf2[5]))
pcf2.pin(1, int(str_pcf2[6]))
pcf2.pin(0, int(str_pcf2[7]))


while True:    
  try:    
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      msg = b'Hello #%d' % counter
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
      limpa_t()
      
    """
    #if bol_limp_t == True:
    if (time.time() - last_message_limp_t) > limp_t_interval:        #ESSE TRECHO FOI CONSTRUIDO PARA LIMPARA A TELA DE TEMPOS EM TEMPOS      
        limpa_t()
        last_message_limp_t = time.time()
        print('limpando tela do display oled...'+str(bol_limp_t));
        bol_limp_t = False
    """
  except OSError as e:
    restart_and_reconnect()


