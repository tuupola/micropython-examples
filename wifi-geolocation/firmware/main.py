# This file is part of MicroPython examples package
# Copyright (c) 2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-examples

from machine import Pin # pylint: disable=import-error
from input import DigitalInput # pylint: disable=import-error
from map import Map # pylint: disable=import-error
from wifi import Wifi # pylint: disable=import-error
from geolocation import Geolocation # pylint: disable=import-error

import ubinascii as binascii # pylint: disable=import-error
import ujson as json # pylint: disable=import-error
import display # pylint: disable=import-error
import m5stack # pylint: disable=import-error

def main():

    zoom = 15
    tft = m5stack.Display()

    tft.text(10, 10, "> Reading settings.\n")
    with open("/flash/settings.json") as fp:
        settings = json.loads(fp.read())

    tft.text(10, tft.LASTY, "> Connecting to wifi.\n")
    wifi = Wifi(settings["username"], settings["password"])

    tft.text(10, tft.LASTY, "> Scanning networks.\n")
    networks = wifi.scan()

    tft.text(10, tft.LASTY, "> Locating current position.\n")
    geolocation = Geolocation(settings["api_key"], networks)
    coordinates = geolocation.coordinates()

    tft.text(10, tft.LASTY, "> Downloading the map.\n")
    map = Map(coordinates)
    map.save("/flash/map.jpg")

    tft.image(0, 0, "/flash/map.jpg")

    button_a = DigitalInput(
        Pin(m5stack.BUTTON_A_PIN, Pin.IN),
        callback = lambda pin: zoom_in_handler(map, tft)
    )

    button_c = DigitalInput(
        Pin(m5stack.BUTTON_C_PIN, Pin.IN),
        callback=lambda pin: zoom_out_handler(map, tft)
    )

def zoom_in_handler(map, tft):
    map.zoom_in()
    map.save("/flash/map.jpg")
    print(map.zoom)
    tft.image(0, 0, "/flash/map.jpg")

def zoom_out_handler(map, tft):
    map.zoom_out()
    map.save("/flash/map.jpg")
    print(map.zoom)
    tft.image(0, 0, "/flash/map.jpg")

if __name__ == "__main__":
    main()