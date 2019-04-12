from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg=MIMEMultipart()
msg['From']='saikumarhaw@gmail.com'
msg['To']='karthikvg1998@gmail.com'
msg['Subject']='Security Alert'


def email(number):
    body ='<html><head>intrusion has been detected!!!</head><body>\n'
    body+='<br/><br/>'
    body+='<p>'+number+'</p>'
    msg.attach(MIMEText(body,'html'))
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(msg['From'],'passwordgoeshere')
    server.sendmail(msg['From'],msg['To'],msg.as_string())
    server.quit()
#email("karthik")
