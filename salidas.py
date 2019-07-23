# -*- coding: utf-8 -*-
#! /usr/bin/python
import RPi.GPIO as gpio
from manejador_salidas import Manejador_Salidas
from Archivo import Archivo
import time

#time.sleep(120)

port_to_gpio = {"0": 29, "1" : 31, "2": 33, "3": 35}

try:
	arch = open("/home/pi/Desktop/Monitoreo OK/otros/salidas.dat", "r")
	cad = arch.read()
	
	out = Manejador_Salidas()
	out.init_ports()
	
	for i in range(len(cad) - 1):
			
		arch.seek(i)
		read = arch.read(1)
		if (read == "0"):
			out.desactivate_port(port_to_gpio[str(i)])
		else: 
			out.activate_port(port_to_gpio[str(i)])
except:
	pass
