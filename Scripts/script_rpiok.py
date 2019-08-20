import RPi.GPIO as gpio
import time 

#~ time.sleep(30)
gpio.setmode(gpio.BOARD)
gpio.setup(15, gpio.OUT)
gpio.output(15, True)
gpio.setup(16, gpio.OUT)
gpio.output(16, True)
