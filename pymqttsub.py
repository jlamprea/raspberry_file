import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt # importamos libreria mqtt
import time as time # libreria de delay
GPIO.setwarnings(False) # apagamos los mensajes de warning
GPIO.setmode(GPIO.BCM) # Vamos a utilizar los puertos se nombran por GPIO
GPIO.setup(4,GPIO.OUT) # gpio4 como salida
GPIO.output(4,GPIO.LOW)# gpio en bajo
GPIO.setup(2,GPIO.IN, pull_up_down = GPIO.PUD_UP)# gpio2 como entrada con resistencia pullup


def on_message(client,userdata,message): # llama cuando hay un mensaje desde el broker
     print("mensaje recibido", str(message.payload.decode("utf-8")))
     print("topic :", message.topic)
     print("mensaje qos: ", message.qos)
     print("mensaje flag retencion: ", message.retain)
    
def on_connect(client,userdata, flags, rc): # llamada cuando hay una coneccion con cliente
    client.subscribe("raspi/gpio3")

client = mqtt.Client("pithon") # se crea una instancia con nombre.
client.connect("192.168.1.60",1883,60)# IP del broker, puerto, tiempo de espera
client.on_connect = on_connect # funcion para estar revisando el sub
client.on_message = on_message # funcion para ver mensaje y banderas
client.subscribe("raspi/gpio3") # se suscribe al topic
client.loop_start() # inicio un nuevo hilo para recibir mensajes


try: # para trabajar las excepciones del programa
    
    while True:
        client.publish("raspi/gpio2","puerto gpio5") # publica el mensaje
        #client.disconnect()
        time.sleep(3)
except KeyboardInterrupt: # cuando se da en el teclado clt x para cerrar. desconecta el cliente
    
    client.loop_stop()
    client.disconnect()