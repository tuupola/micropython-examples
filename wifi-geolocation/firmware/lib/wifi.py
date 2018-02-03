# This file is part of MicroPython examples package
# Copyright (c) 2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-examples

import urequests as requests # pylint: disable=import-error
import network # pylint: disable=import-error

class Wifi(object):

    def __init__(self, username, password):
        self.station = self.connect(username, password)

    def connect(self, username, password):
        station = network.WLAN(network.STA_IF)
        station.active(True)
        station.connect(username, password)

        while not station.isconnected():
            pass

        return station

    def scan(self):
        return self.station.scan()
