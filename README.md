# TrackerFinder

Capture AX25 messages sent by a LASP VHF tracker.

The messages are displayed in a GUI presentations. They are 
also saved in text and raw data files.

## Installation 

You can download this repository and work from there. But better yet, you can 
use pip to install it and then run the module:

```
pip3 install git+https://github.com/MisterMartin/TrackerFinder
    
python3 -m TrackerFinder -h
usage: __main__.py [-h] [-d DEVICE] [-l LOCATION]

Capture AX25 messages sent by a LASP VHF tracker. The two Tracker message types, APRS and position encoded pings, are decoded. Raw and decoded
messages are logged to .raw and .log files.

optional arguments:
  -h, --help            show this help message and exit
  -d DEVICE, --device DEVICE
                        APRS device (default: /dev/tty.TH-D74)
  -l LOCATION, --location LOCATION
                        Location of the log files (default: /Users/charlie/)

The messages are typically delivered via the KISS APRS link over Bluetooth, from a handheld radio. The operating system serial device name is
likely to be different than the default values provided here. Use 'python -m TrackerFinder.portlist' to display a list of available serial ports.
```
