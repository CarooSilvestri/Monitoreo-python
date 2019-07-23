from os import remove
import time
import datetime

yesterday = datetime.date.today() - datetime.timedelta(days=1)

try:
	remove("/home/pi/Desktop/Monitoreo OK/fallas/Fallas " + yesterday.strftime('%d%m%y')	+ ".csv")
except:
	pass
