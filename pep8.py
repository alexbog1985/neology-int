import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"


class Email:
    def __init__(self, login, password, header=None):
        self.login = login
        self.password = password
        self.msg = MIMEMultipart()
        self.header = header

    # send message
    def send_message(self, subject, recipients, message):
        self.msg['From'] = self.login
        self.msg['To'] = ', '.join(recipients)
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(message))
        
        self.ms = smtplib.SMTP(GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        self.ms.ehlo()
        # secure our email with tls encryption
        self.ms.starttls()
        # re-identify ourselves as an encrypted connection
        self.ms.ehlo()
        self.ms.login(self.login, self.password)
        self.ms.sendmail(self.login, self.ms, self.msg.as_string())
        self.ms.quit()
    # send end

    # recieve
    def recieve_message(self):
        self.mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        self.mail.login(self.login, self.password)
        self.mail.list()
        self.mail.select("inbox")
        self.criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        self.result, self.data = self.mail.uid('search', None, self.criterion)
        assert self.data[0], 'There are no letters with current header'
        
        self.latest_email_uid = self.data[0].split()[-1]
        self.result, self.data = self.mail.uid('fetch', self.latest_email_uid, '(RFC822)')
        self.raw_email = self.data[0][1]
        self.email_message = email.message_from_string(self.raw_email)
        self.mail.logout()
    # end recieve


if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None
    
    email = Email(login, password)
    
    email.send_message(subject, recipients, message)
    email.recieve_message()
