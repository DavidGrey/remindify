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

alert = MakeEmail('smtp.gmail.com','davidgreydanus@gmail.com','remindify.bot@gmail.com','def_hacks()','ALERT','Dont forget to sleep!!!!')

alert.send_email()
