import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from secrets import gmail_app_pwd

mail_content = """Hello,
It is night time now. Please lock up your greenhouse.

Thank You!
"""

#The mail addresses and password
sender_address = "shayen.yatagama@gmail.com"
sender_pass = gmail_app_pwd # You will need an App password, if 2 step verification is on!
receiver_address = "shayen.yatagama@gmail.com"

#Setup the MIME
message = MIMEMultipart()
message["From"] = sender_address
message["To"] = receiver_address
message["Subject"] = "Night time! Automated mail sent by Python"
message.attach(MIMEText(mail_content, "plain"))


def send_mail():
    #Create SMTP session for sending the mail
    session = smtplib.SMTP("smtp.gmail.com", 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print("Mail Sent")
