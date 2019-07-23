import subprocess
import time
import socket
import RPi.GPIO as gpio

try:		
	time.sleep(120)
	gpio.setmode(gpio.BOARD)
	gpio.setup(13, gpio.OUT)
	
	socket.gethostbyname('google.com')
	c = socket.create_connection(('google.com', 80), 1)
	if (socket.gethostbyname('google.com') != 0): 
		gpio.output(13, True)
	c.close()
	
except socket.gaierror:
	gpio.output(13, False)
	print ("DNS error")
except socket.error:
	gpio.output(13, False)
	print ("Connection error")
	
except:
	pass
