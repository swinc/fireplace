# Fireplace!

This project creates a battery-powered device which displays a **red light** if there is a Bay Area Spare the Air Day in effect, and a **green light** otherwise.

The project relies on the [Bay Area Air Quality Management District](https://www.baaqmd.gov)'s RSS Feed: https://www.baaqmd.gov/Feeds/AlertRSS.aspx. This RSS feed will give the description `Alert in Effect` during a Spare the Air Day, and `No Alert` otherwise.

## Technical Overview

The project is composed of two main scripts:

1. a python script which runs on a server; and
2. a C program which runs on a microcontroller.

The python script (`fireplace.py`) is run regularly at 3am and 3pm (via crontab) to pull the RSS feed. Depending on the content of the RSS feed, it writes a color (red or green) to a local file inside a web server directory.

The microcontroller periodically wakes and polls the web server to retrieve this file and sets its color based on the contents of the server's file.

## Config

To set details associated with your local environment (including email passwords, etc.), we store these details in a separate file called `config.json` that is ignored and therefore not stored in our Github repo.

When the `fireplace.py` script is run, it opens the `config.json` file and reads in the customized data.

Therefore, upon install, you should open the provided `config-template.json` file, update the details for your environment, and save the file as `config.json` in the top-level directory of this repository.
