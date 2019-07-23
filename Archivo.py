#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import time

class Archivo:

	def __init__(self ):

		self.file = None
		self.nombre = ""

	def abrir_archivo(self, nombre, formato):

		"""Abre el archivo como el formato. Si no existe
		el archivo, lo crea. """
		self.file = open(nombre, formato) #self.nombre


	def guardar_datos(self, p1, p2 = "", p3 = ""):

		"""Guarda los datos recibidos en el archivo."""
		writer = csv.writer(self.file, delimiter = ',')
		escribir = [time.strftime("%d/%m/%y"), time.strftime("%H:%M"), p1, p2, p3,]
		writer.writerow(escribir)
		#~ self.file.write(time.strftime("%d/%m/%y") + "," + time.strftime("%H:%M") + "," + p1 + ","  + p2 + "," + p3 +"\n")


	def cerrar_archivo(self):

		"""Cierra el archivo."""
		self.file.close()

		
