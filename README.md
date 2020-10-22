Door-Connect
=====
Doot-Connect is the IOT platform for door application.

It is base on Meriki MV, Webex Teams and MOXA DIDO.

The aim is provide the integration server for IOT door application.

# Getting Started
There have some hardware equipment and software need to prepare.

* Hardware
    * A Door
    * A Web Server with network.
    *  Meriki Camara
        <p align=center>
        <img src="docs/meraki_mv.png" alt="Meriki Camara" height=200px>
        </p>
    *  MOXA DIDO: IOT connect device
        <p align=center>
        <img src="docs/moxa_dido.png" alt="iot switch" height=200px>
        </p>
    *  Magnetic lock:
        <p align=center>
        <img src="docs/magnetic_lock.png" alt="Magnetic Lock" height=200px>
        </p>
* Environment Setup
    <p align=center>
    <img src="docs/environment.png" alt="env" height=400px>
    </p>

* Software Dependencies on Webserver
    * python3 
    * Flask : Lite weight web server framwork

## Demo Topology
* **Use case1: Who open the door?**
    <p align=center>
    <img src="docs/usercase1.png" alt="usercase1" height=400px>
    </p>
* **Use case2: WHO TOUCH MY BELONGINGS?**
    <p align=center>
    <img src="docs/usercase2.png" alt="usercase2" height=400px>
    </p>

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

