# raspberry_file
Archivos generales para la raspberry

Archivos de aplicacion de la libreria Tkinter, GPIO

Para el usa de los GPIO como entrada utilizando Tkinter. Se debe utilizar interrupciones, ya que el refresco de la ventana no permiete hacer loop para validar el estado de la entrada.

import Tkinter es para python2 
import tkinter en para python3. Usar siempre esta para nuevos proyectos en la raspi.

para startup una aplicacion python con tkinter. se modifica el archivo /etc/profile
Se debe ingrar en la ultima linea el comando sudo python3 /home/pi/Documents/archivo.py
