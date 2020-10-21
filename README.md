Door-Connect
=====
Doot-Connect is the IOT platform for door application.

It is base on Meriki MV, Webex Teams and MOXA DIDO.

The aim is provide the integration server for IOT door application.

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

## License

 is freely redistributable under the BSD 2 clause license. Use of
this source code is governed by a BSD-style license that can be found in the
LICENSE file.

