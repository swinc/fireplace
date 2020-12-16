# Fireplace!

This project is a collection of python and arduino scripts that reports on whether there is a Bay Area Spare the Air day.

## Config

To avoid keeping passwords and other customized details in the public repo, they are stored in a `config.json` file that is not part of the repo.

When the `fireplace.py` script is run, it opens the `config.json` file locally and reads in the customized data.

Therefore, upon install, you must create a file called `config.json` in the top-level directory of this repository and fill out the following fields:

```
{
  "smtp_server": "<your_smtp_server",
  "smtp_port": <port>,
  "sender_email": "<your_sender_email>",
  "recipient_email": "<your_recipient>",
  "password": "<your_password>"
}
```

## RSS Feed

```
<?xml version="1.0" encoding="utf-8" ?>
<rss version="2.0">

<channel>
    <title>Air Alerts for the San Francisco Bay Area</title>
    <link>http://www.sparetheair.org/</link>
    <description>Spare the Air Alert Status</description>
    <language>en</language>
    <lastBuildDate>Tuesday, December 15, 2020 17:25</lastBuildDate>
    <item>
        <title>Spare the Air Status for Tuesday, December 15, 2020</title>
        <date>Tuesday, December 15, 2020</date>
        <description>No Alert</description>
    </item>
</channel>
</rss>
```
