import sys
import os
import re
from dotenv import load_dotenv
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

load_dotenv()

USERNAME = os.environ.get('EMAIL_USERNAME')
PASSWORD = os.environ.get('EMAIL_PASSWORD')

SMTPserver = 'smtp.gmail.com'
from_address = os.environ.get('FROM_ADDRESS')
to_address = [os.environ.get('TO_ADDRESS')]

f = open('message.txt', 'r')
content = f.read()

subject="Sent from Python"

try:
    msg = MIMEText(content, 'plain')
    msg['Subject']=       subject
    msg['From']   = from_address

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(from_address, to_address, msg.as_string())
    finally:
        print('Email sent')
        f.close()
        conn.quit()

except:
    sys.exit( "Email failed: %s" % "CUSTOM_ERROR" )