#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "1.0"

import os
import posixpath
import http.server
import urllib
import cgi
import shutil
import mimetypes
import re
import sys
import json, requests
from urllib.parse import unquote
from urllib.parse import urlparse
from urllib.parse import parse_qs
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import _thread
import time
import datetime
from datetime import datetime,timezone,timedelta

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    server_version = "IOT_Meraki_DevNet_Server/" + __version__

    def do_GET(self):
        """Serve a GET request."""
        parsed = urlparse(self.path)
        print(parsed)
        status_info = parse_qs(parsed.query)['door']
        print(status_info)
        dt0 = datetime.utcnow().replace(tzinfo=timezone.utc)
        print (dt0)
        dt_7 = dt0 + timedelta(hours=-7, seconds=-80)
        dt_7_str = dt_7.strftime("%Y-%m-%d %H:%M:%S")
        print (dt_7_str)
        status_url = self.postToMeraki(dt_7_str)
        print(status_url)
        self.send_response(200)
        self.end_headers()
        self.postToSpark(status_info, status_url, "jiangfzh@cisco.com")
        self.postToSpark(status_info, status_url, "chungchu@cisco.com")
        self.postToSpark(status_info, status_url, "stahuang@cisco.com")


    def postToSpark(self, status_info, status_url, target_addr):
        proxies = {'https': 'http://proxy.esl.cisco.com:80'}
        token = 'OGFhM2IwNDMtZDM1NS00NDMxLWJkOWYtNmFjOWM4OTk4YWNlMTNjMTIyYjItNDhh_PF84_34b868fc-c10b-406f-b3c8-bdd31231a36b'
        headers = {
            'authorization': "Bearer " + token,
            'content-type': "application/json",
            'cache-control': "no-cache",
        }
        payload = "{\"toPersonEmail\":\"" + target_addr + "\"," \
                  "\"text\":\"" + "Door is " + status_info[0] + "\"," \
                  "\"files\":\"" + status_url + "\"}"
        url = 'https://api.ciscospark.com/v1/messages/'
        response = requests.post(url, data=payload, headers=headers, proxies=proxies)
        print (type(response.text))
        print (response.text)
        parsed = json.loads(response.text)
        print (json.dumps(parsed, indent=4, sort_keys=True))
        return False


    def postToMeraki(self, timepoint):
        proxies = {'https': 'http://proxy.esl.cisco.com:80'}
        headers = {
            'X-Cisco-Meraki-API-Key': 'a2e57e3f8c0a9fabd9cd2be56758a9d8c1e919e5',
            'Content-Type': 'application/json',
            'Cookie': '_session_id_for_n189=388a0b6ad6be74bb61c3f9546c076d93'
        }
        payload = "{\n\t\"timestamp\": \"" + timepoint + "\"\n}\n"
        url = 'https://n189.meraki.com/api/v0/networks/N_669347494618033605/cameras/Q2FV-CKH5-WTU4/snapshot'
        response = requests.post(url, data=payload, headers=headers, proxies=proxies)
        print (type(response.text))
        print (response.text)
        parsed = json.loads(response.text)
        print (json.dumps(parsed, indent=4, sort_keys=True))
        url = parsed['url']
        print (url)
        return url



def init_server(http):
    if http:
        httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
    else: # https
        httpd = HTTPServer(('0.0.0.0', 8443), SimpleHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket,
                                       certfile='./server.pem',
                                       server_side=True,
                                       ssl_version=ssl.PROTOCOL_TLSv1)

    httpd.serve_forever()
    httpd.server_close()


VERBOSE = "True"
_thread.start_new_thread(init_server, (True, ))
_thread.start_new_thread(init_server, (False, ))

while 1:
    time.sleep(10)
