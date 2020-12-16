import requests
import re


# pull the daily RSS feed from BAAQMD
r = requests.get('https://www.baaqmd.gov/Feeds/AlertRSS.aspx')

# get all text inside <description> tags (there are two)
matches = re.findall("<description>(.*)</description", r.text)

# pull the second match
status = matches[1]

if(status == "No Alert"):
    print("Green!")
else:
    print("Red")

# send an email with the result
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "<you@email.com>"  # your dev email address
receiver_email = "<recipient@email.com>"  # who you're sending the email too
password = "<your_password>"  # enter your password
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
