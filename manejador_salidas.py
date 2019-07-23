# -*- coding: utf-8 -*-
#! /usr/bin/python
import serial
import RPi.GPIO as gpio

GPIO_29 = 29
GPIO_37 = 37

GPIO_31 = 31
GPIO_32 = 32

GPIO_33 = 33
GPIO_36 = 36
 
GPIO_35 = 35
GPIO_38 = 38

PARES = {29: GPIO_37, 31: GPIO_32, 33: GPIO_35, 35: GPIO_38}

class Manejador_Salidas:
	
	def __init__(self):
		
		gpio.setwarnings(False)
		
		
	def init_ports(self):
		
		"""Inicialization of gpios."""
		
		gpio.setmode(gpio.BOARD)
		gpio.setup(GPIO_29, gpio.OUT)
		gpio.setup(GPIO_37, gpio.OUT)
		
		gpio.setup(GPIO_31, gpio.OUT)
		gpio.setup(GPIO_32, gpio.OUT)
		
		gpio.setup(GPIO_33, gpio.OUT)
		gpio.setup(GPIO_36, gpio.OUT)
		
		gpio.setup(GPIO_35, gpio.OUT)
		gpio.setup(GPIO_38, gpio.OUT)
		

	def activate_port(self, num):
		
		"""if the port is 1, turn the led on = activated"""
		
		gpio.output(num, True)
		gpio.output(PARES[num], True)
		
	def desactivate_port(self, num):
		
		"""if the port is 0, turn off the led = desactivated"""
		
		gpio.output(num, False)
		gpio.output(PARES[num], False)
		
	#~ def change_port_status(self, num):
		
		
		
