#date calculations
import datetime
from dateutil import relativedelta
import ConfigParser


#email sending
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email import Charset
from email.generator import Generator

configname = "example.config"

config = ConfigParser.ConfigParser() 
config.read(configname)

debug = config.get("default", "debug")

mailserver = config.get("mailserver","server")
mailsender = config.get("plenumsmail", "sender")
mailreceiver = config.get("plenumsmail", "receiver") 
mail_reply_receiver = config.get("plenumsmail", "reply_receiver")
invite_text = config.get("plenumsmail", "invite")



invite_subject = config.get("plenumsmail", "subject")

def send_plenums_invite():

    #create the message to be send
    msg = MIMEText(invite_text, 'plain', 'utf-8')
    msg['Subject'] = "%s" % Header(invite_subject, 'utf-8')
    msg['From'] = mailsender
    msg['To'] = mailreceiver
    msg['Reply-To'] = mail_reply_receiver
    
    #send the message
    if not debug:
        s = smtplib.SMTP(mailserver)
        s.sendmail(mailsender, [mailreceiver], msg.as_string())
        s.quit()
    else:
       print msg.as_string() 

                                                                                                


def is_a_plenum_next_tuesday(today):

    #is today a thursday? else. exit, we only send invites on thursdays
    if (today.isoweekday()==4):

        #in 5 days will be a tuesday
        next_tuesday = (today + datetime.timedelta(days=5))
        assert next_tuesday.isoweekday()==2


        #check, if next tuesday is the last tuesday of the month:

        last_tuesday = next_tuesday + relativedelta.relativedelta(day=31, weekday=relativedelta.TU(-1))

        if (next_tuesday == last_tuesday):
            
            #send all the mails!
            return True

        else:
            #nothing to do, next week is a normal chaostreff
            return False

        #TODO: catch AssertError, if today is a thursday, but in 5 days is not a tuesday.
        # This would mean a library broke somewhere
    else:
        #nothing to do. yeah!
        return False

def main():
    today = datetime.datetime.today()
    if is_a_plenum_next_tuesday(today):
        send_plenums_invite()
    else:
        if debug:
            print "no plenum next week"

    #check if file is imported or run on its own:

if __name__ == "__main__":
    main()
