# import smtplib
# 
# from email.mime.text import MIMEText
# 
# server=smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# 
# #from address
# From='chpavankalyan511@gmail.com'
# password='nosj ddjm jxgt xwxs'
# 
# #server login
# server.login(From,password)
# 
# #to address
# To='tangellarevanth0@gmail.com'
# subject='Sending mail using python'
# body='Hello hacker how are you man and how is your fan'
# 
# msg=MIMEText(body)
# msg['From']=From
# msg['To']=To
# msg['subject']=subject
# msg['body']=body
# 
# server.sendmail(From,To,msg.as_string())
# print(f'mail send successfully to {To}')
# 
# server.quit()

'''with Document'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

#from address
From='chpavankalyan511@gmail.com'
password='nosj ddjm jxgt xwxs'

#server login
server.login(From,password)

To='tangellarevanth0@gmail.com'

msg=MIMEMultipart()
msg['from']=From
msg['to']=To
msg['subject']='sending python document'

body='Hello this is python file on email automation'
msg.attach(MIMEText(body,'plain'))
file="C:/Users/LUCKY/Desktop/pfs-039/oops.py"

try:
    with open(file,'rb') as attachment:
        part=MIMEBase('application','octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('content-disposition','attachment',filename='oops.py')
    msg.attach(part)
    server.sendmail(From,To,msg.as_string())
    print('mail sent successfully!')
except Exception as e:
    print(e)
