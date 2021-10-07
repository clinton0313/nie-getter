# nie-getter

A script to automatically fill out info to try to get a nie appointment in Spain.

The default configuration is for getting the "TOMA DE HUELLAS" which is the one you need to do if you are a visiting international student and need to extend your initial NIE visa.  

## Installation

You need to install Selenium and Geckodriver. It runs via Firefox. 

```bash
pip install selenium webdrivermanager python-dotenv geckodriver
```

On MacOSX you can install Geckodriver with:

```bash
brew install geckodriver
```

## Configuration

To configure, copy the `.env.tmpl` to `.env` and edit the values in your favorite editor.

* `MODE` is one of `nie` or `passport`. Different information is needed for each one.

* `COUNTRY` needs to match the form, so for the United States = `EEUU`

* `ALERT_MODE` can run commands to play sounds, etc to notify you when a cita is found

The rest should be pretty self explanatory?

## Usage

```bash
python nie.py
```

This will start a Firefox instance and start running through the pages. Occasionally Firefox may have an infobox about updating to a new version that you will need to manually click on before it will run.

When a cita is found it will make some noise (configurable) and **then you must fill out the form manually to complete the cita**.

## Notes

* The appointments seem to come out at around 8:30am BCN time and new ones continuously pop up until 10:30am. This is just my observation. Also, make sure you leave the expiry date field blank. I had mine filled out to my passport expiry and I never got an appointment for weeks, and then as soon as I left it blank I got one the next day. **Good luck.**

* See: https://github.com/mozilla/geckodriver/releases

* The script can obviously be improved to allow for generally all cases, etc.