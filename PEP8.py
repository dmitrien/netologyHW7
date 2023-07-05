import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailWork:

    def __init__(self):
        self.gmail_smtp = "smtp.gmail.com"
        self.gmail_imap = "imap.gmail.com"
        self.sender_mail = '*****@gmail.com'
        self.sender_password = ''


    def sendMessage(self, recipients: list, subject: str, message_attach: str):
        msg = MIMEMultipart()
        msg['From'] = self.sender_mail
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message_attach))
        ms = smtplib.SMTP(self.gmail_smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.sender_mail, self.sender_password)
        ms.sendmail(self.sender_mail, msg['To'], msg.as_string())
        ms.quit()

    def recieve(self, header=None):
        mail = imaplib.IMAP4_SSL(self.gmail_smtp)
        mail.login(self.sender_mail, self.sender_password)
        mail.list()
        mail.select()
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', header, criterion)
        assert data[0], 'There are no letters with current header'
        mail.logout()

