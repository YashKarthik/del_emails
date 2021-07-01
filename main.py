"""Delete mails using python"""

import imaplib
import email
from email.header import decode_header

uname = 'email@example.com'
pwrd = 'pswd'

imap = imaplib.IMAP4_SSL('imap.example.com')
imap.login(uname, pwrd)

imap.select('INBOX')
status, msg = imap.search(None, 'FROM "spam@spammer.org"')
msg = msg[0].split(b' ')

for mail in msg:
    imap.store(mail, "+FLAGS", "\\Deleted")
    #imap.store(mail, '+X-GM-LABELS', '\\Trash')

imap.expunge()
imap.close()
imap.logout()
