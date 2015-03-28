import json

class MakeEmail(object):
    def __init__(self, SMTPserver, destination, USERNAME, PASSWORD, subject, content):
        self.SMTPserver = SMTPserver
        self.destination = destination
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.subject = subject
        self.content = content

    def send_email(self):
        import sys
        from smtplib import SMTP_SSL as SMTP
        from email.MIMEText import MIMEText
        text_subtype = "plain"
        sender = self.USERNAME
        try:
            msg = MIMEText(self.content, text_subtype)
            msg['Subject'] = self.subject
            msg['From']   = sender # some SMTP servers will do this automatically, not all

            conn = SMTP(self.SMTPserver)
            conn.set_debuglevel(False)
            conn.login(self.USERNAME, self.PASSWORD)
            try:
                conn.sendmail(sender, self.destination, msg.as_string())
                print("Sending")
            finally:
                conn.close()
        except Exception, exc:
            sys.exit( "mail failed; %s" % str(exc) ) # give an error message

with open('../schedule.json') as data_file:
    f = data_file
    data = json.load(data_file)[0]

alert = MakeEmail('smtp.gmail.com',data['email'],'remindify.bot@gmail.com','def_hacks()','Clyde Sinclair Says...',data['message'])

alert.send_email()
