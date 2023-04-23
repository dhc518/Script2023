import smtplib
import email
from email.message import EmailMessage
import mimetypes
import csv

f = open('address.csv', newline='')
reader = csv.reader(f, quotechar="'",
                    delimiter=",",
                    skipinitialspace=True)

import mypass
id = mypass.id
passwd = mypass.passwd

for line in reader: # reader iterator


    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.login(id, passwd)
    msg = EmailMessage()
    msg['Subject'] = '안녕하세요. 반갑습니다.'


    msg['From'] = '메일용<testdragon518@gmail.com>'
    msg['To'] = line[1]  # 'daehyun.lee.python.test@gmail.com'
    msg.set_content(f'''안녕하세요. {line[0]} 님. 반갑습니다.
    저는 두혁찬 이라고 합니다.
    잘 부탁드립니다.
    사진을 첨부했습니다.''')
    with open('dolphin.webp', 'rb') as f:
        msg.add_attachment(f.read(), maintype='image', subtype='webp', filename='dolphin.webp')

    mail_server.send_message(msg)
    mail_server.quit()
    print(line[0])
f.close()



