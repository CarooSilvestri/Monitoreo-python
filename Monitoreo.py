# -*- coding: utf-8 -*-
#! /usr/bin/python
import serial
import csv
import time
import sys

#------------------------------ AUXILIARES

def write_file(arch, p1, p2 = "", p3 = ""):
	
	writer = csv.writer(arch, delimiter = ',')
	escribir = [time.strftime("%d/%m/%y"), time.strftime("%H:%M"), p1, p2, p3]
	writer.writerow(escribir)

def save_errors(error):
	
    ERRORES = open("/home/pi/Desktop/Monitoreo OK/otros/log.csv", "a")
    write_file(ERRRORES, error)
    ERRORES.cerrar_archivo()

def read_data(serial):
	
	v = []
	
	for i in range(0, 7):
		
		c = serial.read(size = 1)
		v.append(c)
		
	return v	
	
# ---------------------------------????
try:
    ser = serial.Serial (
	port = '/dev/ttyS0', #para pi 
	#~ port='COM4', #para windows
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_TWO,
	bytesize = serial.EIGHTBITS,
	timeout=1
    )
	    
except serial.SerialException:
    
    save_errors("SERIAL ERROR: Not Conected")
    

    
#------------------------ ppal
            
def LeoPort():
	
	try:
		while (ser.inWaiting() == 7):
			
			ARCHIVO = open("/home/pi/Desktop/Monitoreo OK/fallas/Fallas" + " " + time.strftime("%d%m%y") + ".csv", "a")
			#~ print(ser.read())
			v = read_data(ser)
			print(v)
			p1 = str(int.from_bytes(v[1], byteorder='big'))
			p2 = str(int.from_bytes(v[2], byteorder='big'))
			p3 = str(int.from_bytes(v[3], byteorder='big'))
				
			if (v[0] == b'S' and v[6] == b'\xaa'):
						
				write_file(ARCHIVO, p1, p2, p3)
				ARCHIVO.cerrar_archivo()     #cierra el archivo
					
	except:
		pass


while 1:
    
    LeoPort()                 #lee continuamente puerto COM
