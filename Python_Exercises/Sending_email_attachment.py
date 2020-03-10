import os
import getpass
import re
import sys
import smtplib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_email(sender, recipient):
	'''Send Email Message'''
	msg = MIMEMultipart()
	msg['To'] = recipient
	msg['From'] = sender
	subject = input("Enter your email subject: ")
	msg["Subject"] = subject
	message = input("Enter your email message.Press Enter when done. ")
	part = MIMEText('text', 'plain')
	part.set_payload(message)
	msg.attach(part)
	#Attach an image in the current directory
	filename = input("Enter the file name of a GIF Image: ")
	path = os.path.join(os.getcwd(), filename)
	if os.path.exists(path):
		img = MIMEImage(open(path,'rb').read(),_subtype="gif")
		img.add_header("Content-Disposition", "attachment", filename=filename)
		msg.attach(img)
	#Create SMTP session
	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	session.ehlo()
	session.starttls()
	session.ehlo()
	password = getpass.getpass(prompt="Enter your email password: ")
	#Login to server
	session.login(sender, password)
	#Send Email
	session.sendmail(sender, recipient, msg.as_string())
	print("Your email is sent to {0}.".format(recipient))
	session.quit()

if __name__ =="__main__":
	sender = input("Enter sender email address: ")
	recipient = input("Enter recipient email address: ")
	send_email(sender, recipient)
