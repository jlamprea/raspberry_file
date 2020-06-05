# Programa para generar una ventana de control de un LED por GPIO
# El texto comentario no debe tener tildes ni signos
#import Tkinter as tk
from Tkinter import * # se importa la libreria completa tkinter para python3
import RPi.GPIO as GPIO # se importa la libreria para control de los pines GPIO
import tkFont # se importa las fuentes de letras para python2
import time
GPIO.setwarnings(False)
#time.sleep(18)
GPIO.setmode(GPIO.BOARD) # se configura para nombrar los pines por su numero (NO GPIO)
GPIO.setup(7,GPIO.OUT) # Se configura como salida
GPIO.output(7,GPIO.LOW) # se configura en Bajo la salida
GPIO.setup(3,GPIO.IN, pull_up_down = GPIO.PUD_UP) # entrada
Cuenta =0 # Variable de conteo, en la funcion se usa global
texto =0 # variable del texto

win =Tk() # se crea la ventana nueva
# se crea la fuenta que se va usar
fuenteletra= tkFont.Font(family= "Helvetica",size=28, weight = "bold")
# Funcion al oprimir un boton
TextoCuenta = StringVar() # Al cambiar el string, actualiza automaticamente la ventana
TextoCuenta= "Conteo:"
TextoConteo= Label(win,text= TextoCuenta)
TextoConteo.pack()
TextoConteo.config(fg="blue",bg= "white",font= ("Helvetica",28))


def Conteo(texto):
    global Cuenta # de declara la variable global para llevar el conteo
    TextoCuenta = "Conteo :" + str(Cuenta) # se arma el texto a mostrar
    TextoConteo.config(text= TextoCuenta) # se actualiza el texto del label a mostrar
    Cuenta = int(Cuenta) +1 # se aumenta la variable
 

def LedON():
    print ("Boton LED Precionado")
    if GPIO.input(7):
        GPIO.output(7,GPIO.LOW)
        print ("Pin 7 en Bajo")
        ledButton ["text"]= "LED ON"
    else:
        GPIO.output(7,GPIO.HIGH)
        print("Pin 7 en alto")
        ledButton["text"]= "LED OFF"
        
# funcion al oprimir un boton        
def salir():
    print("Salir presionado")
    GPIO.cleanup() # limpia los registros del puerto GPIO
    win.quit()# Cierra la ventana nueva
    
win.title("Ventana Prueba") # titulo de la ventana
win.geometry("600x380") # tamano de la ventana en pixels

# Se crea el boton de salir para ejecutar la funcion correspondiente
exitButton = Button(win, text= "SALIR", font = "fuenteletra",command = salir, height = 2, width = 6)
# ubicacion del boton  abajo de la ventana
exitButton.pack(side = BOTTOM)
# se crea el boton de cambio de led con su funcion correspondiente
ledButton = Button(win, text = "LED ON",font= "fuenteletra",command = LedON, height = 2, width = 8)
# ubicacion del boton
ledButton.pack()
# se declara el pin 3 como interrupcion al flanco de bajada con un tiempo de 200ms para evitar rebotes de contacto
# llama la funcion Conteo cada vez que se de un pulso
GPIO.add_event_detect(3,GPIO.FALLING,callback= Conteo,bouncetime=200)    


mainloop() # ciclo de modo grafico
            
    
