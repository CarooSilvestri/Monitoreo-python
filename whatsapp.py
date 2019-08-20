from twilio.rest import Client
import csv
import sys

ASCENSOR = sys.argv[1]
EVENTO = sys.argv[2]
print(len(sys.argv[2]))
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
to_whatsapp_number='whatsapp:+5491138505351'

aux = EVENTO
if(len(EVENTO) == 1): EVENTO = '0' + str(aux)

if (EVENTO in all_fallas):
    
    msg_evento =', Evento ' + EVENTO + ' - ' + all_fallas[EVENTO]
    msg = 'Edificio01: Ascensor ' + ASCENSOR + msg_evento + ', Pos ' + POS
    client.messages.create(body=msg,
						   from_=from_whatsapp_number,
						   to=to_whatsapp_number)



