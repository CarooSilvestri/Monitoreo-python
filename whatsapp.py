from twilio.rest import Client
import csv
import sys

ASCENSOR = sys.argv[1]
EVENTO = sys.argv[2]
POS = sys.argv[3]

all_fallas = {}

def cargar_fallas():
    
    with open('/home/pi/Desktop/Monitoreo OK/otros/Codigos de falla.csv', "r") as f:
        
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
        
            if (row[0] not in all_fallas):
                all_fallas[row[0]] = row[1]
        f.close()
            
                
cargar_fallas()
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+5491138505351'

if (EVENTO in all_fallas):
    
    msg = 'Edificio01: Ascensor ' + ASCENSOR + ', Evento ' + EVENTO + ' - ' + all_fallas[EVENTO] + ', Pos ' + POS
    client.messages.create(body=msg,
						   from_=from_whatsapp_number,
						   to=to_whatsapp_number)

#AC8717a1063bb406bddc1be30d1a2e47e1  	#account sid

#c978c745c1ab7aed2df4b8bb9b5f1b04		#auth token

#export TWILIO_ACCOUNT_SID='AC8717a1063bb406bddc1be30d1a2e47e1' # paste in Account SID between single quotes

#export TWILIO_AUTH_TOKEN='c978c745c1ab7aed2df4b8bb9b5f1b04' # paste Auth Token between single quotes

