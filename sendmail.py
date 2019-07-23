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
TO_EMAIL = 'silconito@gmail.com'
FROM_PWD    = 'edi@pru01'
SMTP_SERVER = 'imap.gmail.com'


m = Mail(TO_EMAIL, "Fallas" + " " + time.strftime("%d/%m/%y"))
m.create_initialize_server()
m.login()
m.attach_file()
m.send_mail()
m.quit_server()
