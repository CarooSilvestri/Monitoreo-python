#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
import time
import imaplib
import sys
import email
from Mail import Mail
from manejador_salidas import Manejador_Salidas


FROM_EMAIL  = 'edificio.prueba.01@gmail.com'
FROM_PWD    = 'edi@pru01'
SMTP_SERVER = 'imap.gmail.com'

arch = open("/home/pi/Desktop/Monitoreo OK/otros/salidas.dat", "r+")
cad = arch.read()
MAN = Manejador_Salidas()
MAN.init_ports()

GPIO_29 = 29
GPIO_31 = 31
GPIO_33 = 33
GPIO_35 = 35

POS = {GPIO_29: 0, GPIO_31: 1, GPIO_33: 2, GPIO_35: 3}	


def comand_on(port):
	
	arch.seek(POS[port])	
	arch.write("1")
	MAN.activate_port(port)
	
def comand_off(port):

	arch.seek(POS[port])	
	arch.write("0")
	MAN.desactivate_port(port)


COMANDOS = {'FDS ON': [comand_on, GPIO_29], 'FDS OFF': [comand_off, GPIO_29],
			'COMANDO2on': [comand_on, GPIO_31], 'COMANDO2off': [comand_off, GPIO_31],
			'COMANDO3on': [comand_on, GPIO_33], 'COMANDO3off': [comand_off, GPIO_33],
			'COMANDO4on': [comand_on, GPIO_35], 'COMANDO4off': [comand_off, GPIO_35]}


def reply_comands(para, asunto = "Comando recibido"):

	m = Mail(para, asunto)
	m.create_initialize_server()
	m.login()
	if (asunto == "INFO"): m.attach_file()
	m.send_mail()
	m.quit_server()
	


def read_email_from_gmail():
	
	mail = imaplib.IMAP4_SSL(SMTP_SERVER)
	mail.login(FROM_EMAIL,FROM_PWD)
	mail.select('INBOX')
	
	result, data = mail.search(None, 'UnSeen')	
	
	mail_ids = data[0] 	
	id_list = mail_ids.split()
	
	try:
		first_email_id = int(id_list[0])
		latest_email_id = int(id_list[-1]) 	# get the latest
		
		for i in range(first_email_id,latest_email_id+1):
			
			typ, data = mail.fetch(str(i), "(RFC822)" ) # fetch the email body (RFC822)  
			for response_part in data:
				
				 if isinstance(response_part, tuple):
					 
					 msg = email.message_from_string(response_part[1].decode("utf-8"))
					 subject = msg['Subject']             
					 de = msg['From']
					 para = (de.split(">"))[0].split("<")
					 
					 if (subject.upper() == "INFO"):
						 
						 reply_comands(para[1], "INFO")					 
					
					 elif (subject.upper() in COMANDOS):
					
						 COMANDOS[subject.upper()][0](COMANDOS[subject.upper()][1])
						 reply_comands(para[1])
						 break
		sys.exit()
		
	except IndexError:
		raise IndexError
				

def main():
	
	while True:
		
		try:
			read_email_from_gmail()
			
		except IndexError:
			break			
			
main()
