# With this program you can send emails via your gmail account #

### Gmail Account Details of sender email need to be changed in config.py
### Make sure to allow usage of "Less Secure Apps" in gmail (see below URL),
### otherwise the python script will be identified as insecure and blocked by gmail
### http://myaccount.google.com/lesssecureapps

import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

body = "Hi fellows, this Email is sent from my Python Script"
subject = "Email via Python"

msg = MIMEMultipart()
msg['From'] = config.mailfromAdress
msg['To'] = config.mailtoAdress
msg['Subject'] = subject

msg.attach(MIMEText(body,'plain'))
message = msg.as_string()

try:
    server = smtplib.SMTP(config.mailServer)
    server.starttls()
    server.login(config.mailfromAdress, config.mailfromPassword)

    server.sendmail(config.mailfromAdress, config.mailtoAdress, message)
    server.quit()
    print("SUCCESS - Email sent")

except Exception as e:
    print("FAILURE - Email not sent")
    print(e)
