import requests, re, json


# pull the daily RSS feed from BAAQMD
r = requests.get('https://www.baaqmd.gov/Feeds/AlertRSS.aspx')

# get all text inside <description> tags (there are two)
matches = re.findall("<description>(.*)</description", r.text)

# pull the second match
status = matches[1]

color = "red"

if(status == "No Alert"):
    color = "green"

# send an email with the result
import smtplib, ssl

with open('../config.json') as f:
  config = json.load(f)

smtp_server = config["smtp_server"]
port = config["smtp_port"]
sender_email = config["sender_email"]
receiver_email = config["recipient_email"]
password = config["password"]
message = f"""\
Subject: Spare the Air Day Alert

The light is {color}."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
