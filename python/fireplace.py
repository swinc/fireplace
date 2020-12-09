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
