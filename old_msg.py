from os import listdir, remove
from os.path import isfile, isdir
from Mail import Mail
import time

FROM_EMAIL  = 'edificio.prueba.01@gmail.com'
TO_EMAIL = 'silconito@gmail.com'
FROM_PWD    = 'edi@pru01'
SMTP_SERVER = 'imap.gmail.com'
ARCH_DIA = "Fallas" + " " + time.strftime("%d%m%y") + ".csv" 

def ls1(path):    
    return [obj for obj in listdir(path)]
    
def send_old_msg(path):
    
    l_files = ls1(path)
    if (len(l_files) <= 1): return 
    else: 
        m = Mail(TO_EMAIL, "Fallas remanentes")
        m.create_initialize_server()
        m.login()
        if (ARCH_DIA in l_files): 
            l_files.remove(ARCH_DIA)
            
        for f in l_files:
            m.attach_file(f)
            remove(path + f)

        m.send_mail()
        m.quit_server()
            
time.sleep(60)
send_old_msg("/home/pi/Desktop/Monitoreo OK/fallas/")
