import BlynkLib
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # con Blynk los puertos se nombran por GPIO
GPIO.setup(4,GPIO.OUT) 
GPIO.output(4,GPIO.LOW)
GPIO.setup(2,GPIO.IN, pull_up_down = GPIO.PUD_UP)
auth_token= "tdA72mGXbO-tBx-5qYo54v4-qo7zBtC1"
blynk = BlynkLib.Blynk(auth_token)

# se conecta una led al pin 7 GPIO4 y se control por
# un boton al pin virtual 4 en la app blynk
@blynk.VIRTUAL_WRITE(4) # V4 es el pin del Boton en la app blynk
def control_write_handler(value):
  pinValue = int(value[0]) # el valor esta en una lista pos 0
  if pinValue ==1:
      GPIO.output(4,GPIO.HIGH) # se activan los puertos GPIO4 pin7
      blynk.virtual_write(1,255) # prende el piloto LED al max en app
      blynk.virtual_write(2,"Led prendido")
  else:
      GPIO.output(4,GPIO.LOW)
      blynk.virtual_write(1,0)
      blynk.virtual_write(2,"Led Apagado")
@blynk.VIRTUAL_WRITE(3) # V esta el sensor de proximidad de la app
def proxi_wite_handler(value):
    pin_prox = value[0]
    print("el valor del sensor es: {}".format(pin_prox))

#loop de Blynk
while True:
    if GPIO.input(2)==0:
        # escribe un tweet
        blynk.tweet("Pruebas de Raspi con IoT Blynk @Jlampreainge")
        blynk.notify("pin 3 Entrada en bajo") # se escribe en la widget notify de la app
    blynk.run()

