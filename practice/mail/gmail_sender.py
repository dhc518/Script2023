import smtplib
import email
from email.message import EmailMessage
import mimetypes

import mypass

id = mypass.id
passwd = mypass.passwd

mail_server = smtplib.SMTP('smtp.gmail.com', 587)
mail_server.ehlo()
mail_server.starttls()
mail_server.login(id, passwd)
msg = EmailMessage()
msg['Subject'] = '두번째 메일 파일 첨부'
msg['From'] = '메일용<testdragon518@gmail.com>'
msg['To'] = 'testdragon518@gmail.com'#'daehyun.lee.python.test@gmail.com'
msg.set_content('나의 두번재 메일')
with open('dolphin.webp', 'rb') as f:
    msg.add_attachment(f.read(), maintype = 'image', subtype = 'webp', filename='dolphin.webp')
    
mail_server.send_message(msg)
mail_server.quit()