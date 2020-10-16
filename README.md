
# Introduction
=======
# IOT-IM-Platform

IOT-IM Platform:

IOT + IM + Cloud = IOT-IM Platform


## Description

This platform is to build a bridge between IOT device and IM tool.

In this platform, IM tool and IOT device can talk to each other.

User can monitor and control IOT device by IM tool anytime and anywhere.

IOT device can send important info to user's IM tool automatically and in time.

In this project, the IOT devices include Meraki camera and MOXA Switch.

IM tool is Webex Teams


## How it works

MOXA Switch detect IOT device's alarm info and send message to IOT-IM webserver.

IOT-IM webserver is triggered to get snapshot from Meraki camera.

IOT-IM webserver send both IOT info and camera snapshot to IM tool.

The Python part server as IOT-IM webserver.


## Install
```bash
pip install python3
python3 IOT_Meraki_DevNet.py
```

