Door-Connect
=====
Door-Connect is the IOT platform for door application.
It will bridge IOT device, IM tool (WebexTeams) and Cloud application.
In this platform, user can monitor the door environment and even get notify when environment change.

Most Enterprises has some confidential places such as file room, operation room, data center and so on. <br />
They need a good solution which can control and record staff who and when enters these kind of rooms. When there is something happened, they need a simple tool which can provide much more visibility and trace back easily.

The platform is base on Meriki MV, Webex Teams and MOXA DIDO hardware and our software integration platform.
The aim is provide the integration server for IOT door application.

# Getting Started
There are some hardware equipment and software need to prepare.
* Environment Setup
    <p align=center>
    <img src="docs/environment.png" alt="env" height=400px>
    </p>
* Hardware Component
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
* How to get a Meraki API Key:<br/>
 There is the instruction under https://developer.cisco.com/meraki/api/#!authorization/obtaining-your-meraki-api-key.
    <p align=center>
        <img src="docs/GetmerakiAPIkey.png" alt="Magnetic Lock" height=200px>
    </p>
* How to create a Webex Bot:<br/>
 This is a create link https://developer.webex.com/my-apps/new/bot
    <p align=center>
        <img src="docs/CreateWebexBox.png" alt="Magnetic Lock" height=200px>
    </p>
* Software Dependencies on Webserver
    * python3 
    * Flask : Lite weight web server framwork
    * Installation
        ```bash
        pip install python3
        ```
## Demo Topology
* **Use case1: Who open the door?**
    <p align=center>
    <img src="docs/usercase1.png" alt="usercase1" height=400px>
    </p>
* **Use case2: WHO TOUCH MY BELONGINGS?**
    <p align=center>
    <img src="docs/usercase2.png" alt="usercase2" height=400px>
    </p>
## How it works
    1. Run the Door-connect on server `python3 IOT_Meraki_DevNet.py`, it will bridge all door application components.
    2. IOT device will keep wating the external event happen.
    3. Once there have event, MOXA DIDO detect IOT device's alarm info and send message to Door-Connect webserver.
    4. Door-Connect webserver is triggered to get snapshot from Meraki camera.
    5. Door-Connect webserver send both IOT info and camera snapshot to Webex Teams (user application).

## License
BSD licensesis freely redistributable under the BSD 2 clause license. Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.

