#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

import smtplib
import time

class Mail:
	
	def __init__(self, to, subject = "Fallas" + " " + time.strftime("%d%m%y")):

		 # create message object instance
		self.msg = MIMEMultipart()

		# setup the parameters of the message
		self.password = "edi@pru01"
		self.msg['From'] = "edificio.prueba01@gmail.com"
		self.msg['To'] = to
		self.msg['Subject'] =  subject
		self.server = None
		
	def create_initialize_server(self):
				
		# create server
		self.server = smtplib.SMTP('smtp.gmail.com: 587')
		
		 # starts the server
		self.server.starttls()
		
	def attach_file(self, name_f="Fallas" + " " + time.strftime("%d%m%y") + ".csv"):
		
		# attach file to message body
		try:
			rut = "/home/pi/Desktop/Monitoreo OK/fallas/"
			f = open(rut + name_f, 'r')
			attachment = MIMEBase('application','octet-stream')
			attachment.set_payload(f.read())
			f.close()
			attachment.add_header('Content-Disposition', 'attachment', filename=name_f)          
			self.msg.attach(attachment)
		except:
			self.attach_cuerpo("No se registraron fallas en el día. Puede eliminar el mensaje.")
			
	def login(self):
		
		# Login Credentials for sending the mail
		self.server.login(self.msg['From'], self.password)
		
	def quit_server(self):
		
		# quits server
		self.server.quit()
		
	def send_mail(self):
		
		# send the message via the server.	
		self.server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
	
	def attach_cuerpo(self, texto):
		
		# agrega el cuerpo al mail
		self.msg.attach(MIMEText(texto))

