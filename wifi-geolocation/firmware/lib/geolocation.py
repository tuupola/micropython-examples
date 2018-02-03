# This file is part of MicroPython examples package
# Copyright (c) 2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-examples

import ujson as json # pylint: disable=import-error
import ustruct as struct # pylint: disable=import-error
import urequests as requests # pylint: disable=import-error

class Geolocation(object):

    def __init__(self, api_key, networks):
        self.api_key = api_key
        self.networks = networks

    def coordinates(self):
        return self.locate()

    def locate(self):
        data = {
            "considerIp": False,
            "wifiAccessPoints": []
        }

        for wifi in self.networks:
            entry = {
                "ssid": wifi[0],
                "macAddress": "%02x:%02x:%02x:%02x:%02x:%02x" % struct.unpack("BBBBBB", wifi[1]),
                "signalStrength": wifi[3],
                "channel": wifi[2]
            }
            data["wifiAccessPoints"].append(entry)

        headers = {"Content-Type": "application/json"}
        url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + self.api_key

        response = requests.post(url, headers=headers, data=json.dumps(data))
        return json.loads(response.content)["location"]

