
import display
from display import*

import pcf8574
from machine import I2C, Pin

#-----------------------------------------------------------------------------------------------------------------------
"""
import ota_updater
from ota_update.main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/Elitec-MrEli/micropython/tree/main')
    ota_updater.download_and_install_update_if_available('elitec_testes_off', '12345678')

#def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...

def boot():
    download_and_install_update_if_available()
    #start()


boot()
"""
#-----------------------------------------------------------------------------------------------------------------------

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
    imprime_oled('REBOOT recebido')
    #--ajustar em uma função
    leia_pinos()      
    msg = b'|reboot..ando|PCF1:' + str(str_pcf1)#REPORTA A PINAGEM DOS PCF
    msg += b'|PCF2:' + str(str_pcf2)#FUTURAS MELHORIAS TEM QUE INCLUIR AS PORTAS DO MICRO    
    client.publish(topic_pub, msg)
    #--ajustar em uma função
    time.sleep(1)
    print('--5--')
    imprime_oled('--5--')
    time.sleep(1)
    print('--4--')
    imprime_oled('--4--')
    time.sleep(1)
    print('--3--')
    imprime_oled('--3--')
    time.sleep(1)
    print('--2--')
    imprime_oled('--2--')
    time.sleep(1)
    print('--1--')
    imprime_oled('--1--')
    time.sleep(1)
    print('reboot__ando...')
    imprime_oled('reboot__ando...')
    machine.reset()
#---------------------------------
  global state 
  if msg == b"1":        
        if str(led.value()) == "1":
            print('led ja ligado')
            imprime_oled('led ja ligado')
        else:
            msg = b'Confirmando... ligando led'
            client.publish(topic_pub, msg)
            print('ligando led')
            imprime_oled('led Lig =L')            
            #bol_limp_t = True
            led.value(1)
            state = 0
  elif msg == b"0":                
        if str(led.value()) == "0":
            print('led ja desligado')
            imprime_oled('led ja desligado')
        else:
            msg = b'Confirmando... desligando led'
            client.publish(topic_pub, msg)
            print('deligando led')
            imprime_oled('led desl =D')             
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
            imprime_oled('invert.led =D')            
            #bol_limp_t = True
        elif state == "0":
            msg = b'Confirmando... invertendo led para ligado'
            client.publish(topic_pub, msg)
            led.value(1)
            state = 0
            print('invertendo led para ligado')
            imprime_oled('invert.led =L')             
            #bol_limp_t = True
  elif msg == b"p101":
      pcf.pin(0, 0)
      imprime_oled('p101 =L') 
  elif msg == b"p100":    
      pcf.pin(0, 1)
      imprime_oled('p100 =D')
  elif msg == b"p111":
      pcf.pin(1, 0)
      imprime_oled('p111 =L')
  elif msg == b"p110":    
      pcf.pin(1, 1)
      imprime_oled('p110 =D')
  elif msg == b"p121":
      pcf.pin(2, 0)
      imprime_oled('p121 =L')
  elif msg == b"p120":    
      pcf.pin(2, 1)
      imprime_oled('p120 =D')
  elif msg == b"p131":
      pcf.pin(3, 0)
      imprime_oled('p131 =L')
  elif msg == b"p130":    
      pcf.pin(3, 1)
      imprime_oled('p130 =D')
  elif msg == b"p141":
      pcf.pin(4, 0)
      imprime_oled('p141 =L')
  elif msg == b"p140":    
      pcf.pin(4, 1)
      imprime_oled('p140 =D')
  elif msg == b"p151":
      pcf.pin(5, 0)
      imprime_oled('p151 =L')
  elif msg == b"p150":    
      pcf.pin(5, 1)
      imprime_oled('p150 =D')
  elif msg == b"p161":
      pcf.pin(6, 0)
      imprime_oled('p161 =L')
  elif msg == b"p160":    
      pcf.pin(6, 1)
      imprime_oled('p160 =D')
  elif msg == b"p171":
      pcf.pin(7, 0)
      imprime_oled('p171 =L')
  elif msg == b"p170":    
      pcf.pin(7, 1)
      imprime_oled('p170 =D')
      
  elif msg == b"p201":
      pcf2.pin(0, 0)
      imprime_oled('p201 =L')
  elif msg == b"p200":    
      pcf2.pin(0, 1)
      imprime_oled('p200 =D')
  elif msg == b"p211":
      pcf2.pin(1, 0)
      imprime_oled('p211 =L')
  elif msg == b"p210":    
      pcf2.pin(1, 1)
      imprime_oled('p210 =D')
  elif msg == b"p221":
      pcf2.pin(2, 0)
      imprime_oled('p221 =L')
  elif msg == b"p220":    
      pcf2.pin(2, 1)
      imprime_oled('p220 =D')
  elif msg == b"p231":
      pcf2.pin(3, 0)
      imprime_oled('p231 =L')
  elif msg == b"p230":    
      pcf2.pin(3, 1)
      imprime_oled('p230 =D')
  elif msg == b"p241":
      pcf2.pin(4, 0)
      imprime_oled('p241 =L')
  elif msg == b"p240":    
      pcf2.pin(4, 1)
      imprime_oled('p240 =D')
  elif msg == b"p251":
      pcf2.pin(5, 0)
      imprime_oled('p251 =L')
  elif msg == b"p250":    
      pcf2.pin(5, 1)
      imprime_oled('p250 =D')
  elif msg == b"p261":
      pcf2.pin(6, 0)
      imprime_oled('p261 =L')
  elif msg == b"p260":    
      pcf2.pin(6, 1)
      imprime_oled('p260 =D')
  elif msg == b"p271":
      pcf2.pin(7, 0)
      imprime_oled('p271 =L')
  elif msg == b"p270":    
      pcf2.pin(7, 1)
      imprime_oled('p270 =D')
  elif msg == b"ptof":    
      pcf.port = 0xff
      pcf2.port = 0xff
      imprime_oled('ptof =D Tudo')
  elif msg == b"pton":    
      pcf.port = 0
      pcf2.port = 0
      imprime_oled('pton =L Tudo')
  elif msg == b"p1t3":    
      pcf.pin(3, 0)
      imprime_oled('p1 io3 =L')
      print('pulso de 3 seg pcf1 porta 3')      
      time.sleep(1)
      imprime_oled('p.3s.p1 io3')
      time.sleep(0.3)
      print('.')
      imprime_oled('p.3s...3')
      time.sleep(1)
      print('.')
      imprime_oled('p.3s...2')
      time.sleep(1)
      print('.')
      imprime_oled('p.3s...1')
      pcf.pin(3, 1)
      imprime_oled('p1 io3 =D')
  elif msg == b"p2t3":
      imprime_oled('p2 io3 =L')
      pcf2.pin(3, 0)
      print('pulso de 3 seg pcf2 porta 3')
      time.sleep(1)
      imprime_oled('p.3s.p2 io3')
      time.sleep(0.3)
      print('.')
      imprime_oled('p.3s...3')
      time.sleep(1)
      print('.')
      imprime_oled('p.3s...2')
      time.sleep(1)
      print('.')
      imprime_oled('p.3s...1')
      pcf2.pin(3, 1)
      imprime_oled('p2 io3 =D')
#---------------------------------          
      
def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Conectado no MQTT %s, INSCRITO no TOPICO %s PUBLICANDO no TOPICO %s' % (mqtt_server, topic_sub, topic_pub))
  imprime_oled('Conectad. MQTT!')
  msg = b'Cheguei id:' + str(client_id)
  client.publish(topic_pub, msg)
  return client

def restart_and_reconnect(): # AQUI PARECE QUE O WHILE TRUE: FAZ UMATIVA DE PUB E SUB, COSO TIVER ERROS EXECUTA ESTA FUNÇÃO QUE COMUNICA FALHA E REBOOTA
  print('FALHA AO CONECTAR AO SERVER MQTT "'+ str(mqtt_server) +'" Reconectarei em...'+str(tempo_antes_reiniciar_por_falha_mqtt)+'Seg')
  imprime_oled('Falha Conec.MQTT')
  time.sleep(1)
  global t_
  t_ = tempo_antes_reiniciar_por_falha_mqtt - 1  
  for numero in range(t_):    
        print(numero - t_)
        imprime_oled(str(numero - t_))
        time.sleep(1) # AGUARDA '60' SEGUNDOS E REINICIA  
  #machine.reset() # REINICIA O ESP... 
  reb_.value(1) #começa com sistema ativado se deslgar essa porta o esp desliga
  time.sleep(2)
  reb_.value(0)
try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

limpa_t()
inicializacao() #4 SEG DE ELITEC


leia_pinos()
#print('PCF1:|'+str_pcf1[0]+'-'+str_pcf1[1]+'-'+str_pcf1[2]+'-'+str_pcf1[3]+'-'+str_pcf1[4]+'-'+str_pcf1[5]+'-'+str_pcf1[6]+'-'+str_pcf1[7]+'|')
pcf.pin(7, int(str_pcf1[0]))
pcf.pin(6, int(str_pcf1[1]))
pcf.pin(5, int(str_pcf1[2]))
pcf.pin(4, int(str_pcf1[3]))
pcf.pin(3, int(str_pcf1[4]))
pcf.pin(2, int(str_pcf1[5]))
pcf.pin(1, int(str_pcf1[6]))
pcf.pin(0, int(str_pcf1[7]))

#print('PCF2:|'+str_pcf2[0]+'-'+str_pcf2[1]+'-'+str_pcf2[2]+'-'+str_pcf2[3]+'-'+str_pcf2[4]+'-'+str_pcf2[5]+'-'+str_pcf2[6]+'-'+str_pcf2[7]+'|')
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
      leia_pinos()  
      msg =  b'Hello#%d' % counter
      msg += b'|PCF1:' + str(str_pcf1)#REPORTA A PINAGEM DOS PCF
      msg += b'|PCF2:' + str(str_pcf2)#FUTURAS MELHORIAS TEM QUE INCLUIR AS PORTAS DO MICRO
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


