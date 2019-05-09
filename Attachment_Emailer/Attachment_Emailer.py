#! /usr/bin/python3.5

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from = '<USER>@company.com', send_to = ['<USER>@company.com'], subject='PFA', text, files,server="localhost"):

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()



if __name__ == '__main__':

    my_files = ['/home/<USER>/Results.xls']

    send_mail(send_from = '<USER>@company.com', send_to = ['<USER>@company.com'], subject = 'Python Attachement check', text = 'Hello world!!', files = my_files, server = 'localhost')
