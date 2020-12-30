# ==== import libraries we are using ====
import requests  # for http requests (e.g., pulling the RSS feed)
import re        # for searching with regular expressions
import json      # for reading config.json file
import os        # for file system path names
import smtplib   # for sending email
import ssl       # for making encrypted connection to send email
import socket    # for obtaining our host IP address

# ==== pull the RSS feed ====
r = requests.get('https://www.baaqmd.gov/Feeds/AlertRSS.aspx')
matches = re.findall("<description>(.*)</description", r.text)  # match text inside <description> tags (there are two)
status = matches[1]  # grab the second match

if status == "No Alert":
    color = "green"
elif status == "Alert In Effect":
    color = "red"
else:
    color = "no match"  # in future, only send email on no match

# ==== get config details ====
path_to_config = os.path.dirname(os.path.realpath(__file__)) + '/../config.json'
with open(path_to_config) as f:
    config = json.load(f)

# ==== write result to file ====
f = open(config["path_to_www_file"], "w")
f.write(color)
f.close()

# ==== get our IP address (see https://cutt.ly/Dh10wYW) ====
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('10.255.255.255', 1))
host_ip = s.getsockname()[0]

# ==== send an email with the result ====
www_file = os.path.basename(config["path_to_www_root"])
message = f"""\
Subject: Fireplace Alert!

The light should be {color}.

Color has been written to: http://{host_ip}/{www_file}"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(config["smtp_server"], config["smtp_port"], context=context) as server:
    server.login(config["sender_email"], config["password"])
    server.sendmail(config["sender_email"], config["recipient_email"], message)
