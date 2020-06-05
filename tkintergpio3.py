
#programa con tkinter para Python3
import tkinter as tk # libreria para python3
import RPi.GPIO as GPIO # se importa la libreria para control de los pines GPIO
from tkinter import font
#import tkFont # se importa las fuentes de letras para python2
from tkinter import ttk # importa libreria toolkits para tkinter
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # se configura para nombrar los pines por su numero (NO GPIO)
GPIO.setup(7,GPIO.OUT) # Se configura como salida
GPIO.output(7,GPIO.LOW) # se configura en Bajo la salida
GPIO.setup(3,GPIO.IN, pull_up_down = GPIO.PUD_UP) # entrada
Cuenta =0 # Variable de conteo, en la funcion se usa global
texto =0 # variable del texto
win= tk.Tk()
fuenteletra= font.Font(family= "Helvetica",size=28, weight = "bold")
# Funcion al oprimir un boton
TextoCuenta = tk.StringVar() # Al cambiar el string, actualiza automaticamente la ventana
TextoCuenta= "Conteo:"
TextoConteo= tk.Label(win,text= TextoCuenta)
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
exitButton = tk.Button(win, text= "SALIR", font = "fuenteletra",command = salir, height = 2, width = 6)
# ubicacion del boton  abajo de la ventana
exitButton.pack(side = tk.BOTTOM) # Se puede colocar con "bottom"
# se crea el boton de cambio de led con su funcion correspondiente
ledButton = tk.Button(win, text = "LED ON",font= "fuenteletra",command = LedON, height = 2, width = 8)
# ubicacion del boton
ledButton.pack()
# se declara el pin 3 como interrupcion al flanco de bajada con un tiempo de 200ms para evitar rebotes de contacto
# llama la funcion Conteo cada vez que se de un pulso
GPIO.add_event_detect(3,GPIO.FALLING,callback= Conteo,bouncetime=200)    


tk.mainloop() # ciclo de modo grafico

# para iniciar el programa automanticamente hacer:
# comandos:
# cd /etc
# sudo nano profile   ->editarr el archivo profile
# en la ultima linea anexar lo siguiente
# python3 /home/pi/Documents/tkintergpio3.py
# guardar y salir.
# estoy ejecuta el programa .py despues que se han cargado las librerias de graficos
# del sistema operativo, por eso no funciona el comando crontab.
# crontab solo funciona para ejecutar archivos  de python sin graficos.