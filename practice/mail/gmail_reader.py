import imapclient
import email
from email.policy import default

imap_server = imapclient.IMAPClient('imap.gmail.com', ssl=True)

import mypass
id = mypass.id
passwd = mypass.passwd

imap_server.login(id, passwd)
imap_server.select_folder('INBOX')
messages = imap_server.gmail_search('')#모든 메일
imap_server.logout()