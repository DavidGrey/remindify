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
            finally:
                conn.close()
        except Exception, exc:
            sys.exit( "mail failed; %s" % str(exc) ) # give an error message

with open('../sample-schedule.json') as data_file:
    f = data_file
    data = json.load(data_file)[0]

alert = MakeEmail('smtp.gmail.com',data['email'],'remindify.bot@gmail.com','def_hacks()','Clyde Sinclair Says...','>>> '+data['message']+' <<<'+'\n'*6+"""
                                                                  .$            
                                                            ..+MM$7MMD          
                                                    .M7. .M777777777M7I         
                                                  .M7M$7$MM777MMMM:::MM         
                                              ..MM$7ZMZMM7MMMM7MOM:$II?         
                       ....                 ..777M7MMZM7ZMMMZ7:MMM:??II         
              ....~MMM$77777M$....     .....M$M7777MMMMMMMM7MIIMMD=?III.        
             +M7MMMMMMMM7MMM77777M     M7$MM$M7M7$MMMMM$7M~I~OI?II.7?II         
          N77$MMMM7OMMMMMMMM7777$MM77777MM$MM7MZ7MMMMM7M=::::.?MMM  ?II.        
       .MM7OMM7MMMM7ZMMM8$ZOMMMMM777MMMMMMM77MM7MMM$7MM:::M.. DI?M. ?I?         
    . MMMMMMMMMMMMM$777MMMMMMM77MMMMMMMMM77MM77MM77:M:::~.    .I?I. ?IM         
   .MMM77M77MMM77OMMMMMM77MMMM77OMM$7777MMMMMMM78~M::::N.     .ZMM  ?I.         
   =7MMM7777M77MMMMMMMMMMMM77DZ$MMMMM7$77MMMMM7MN::::~.       .? .  ?8.         
 ..77MM77777MMMMMMM7777777$7M7777777M77MM$7$M::~:::::.        .     =.          
 .M7MMMMM77MMMM7777Z77O7M777M77Z7$77Z77:::MMM:::::::D              ...          
 .O7MMMM77MMM7$77M7777M$M77MM7M7NM77$7O:MMDMMM:::::=7.                          
  7MM77M7MMM7M77M7MMM....  .?MM77M7N777~:=MM=OZZ:::::7.                         
 .7ZM7M7MMM7777M.              .,M7MM$MM:::I+ZZZZZZ::M8.                        
 ~7M777MMMM7777.                   .,MMMO:M~MM:ZZZZZ~:$M.                       
 I$MMMMMMM77$7M                       .MZ7:M:::::MZZZMD7.     .M                
  M7MMMMMM777MZ.                       .M$$~OM~::::ZZZM$M..   .?                
  MMM7MMM7777MMM.                       ..MZM:M7::::$ZZMM$....M?.               
   MM7MM$77777M7.                          M77:7=::::?MZZM=7DZI?.               
   .MM$MM$77M777O                           .M7OM:::O?MDZZZM~:?M.               
    M7M7M77M7M77$M                            .M7MM:IIM:::ZZZ::77:              
    .M7MM7$MMM7MM77N                            ..M7M?M::::~OZM:7M              
     .7M777MMMMMM7MMM..                             M7O7MO::~~MZ$...            
      Z$MM7MMMM7777777M.                                ~MMMMMM..ZZ...          
       M7MMMM77MMIMMMMMM..                                        .Z$..         
       ?M$MM77777MMMMMMMM8                                        ..ZZ          
        MM7M77$7M77$7NMMMNM                                         MZZ.        
        M7NM7777$MM777$MM7M+                                         ZZM.       
        .N$ZMMM77M7MMM7MM7MM.                                        .ZZ=       
         .MMMMM$77$M7NMM7MMM                                          MZZM.     
          MMMMMM7MM7MM7M77$MM                                          MZMZD. . 
           MMMMM77MMMM7MM7M7M                                            ZZDM. 
           .M777MM7MM777N7M7                                             ..MM.. 
            . MZMM777$MMMM7M                                               .. . 
               .MMM7MMZ777M.                                                    
                  MMMMMMM                                                       
                     ..                                                         
""")

alert.send_email()
