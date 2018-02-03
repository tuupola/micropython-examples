# This file is part of MicroPython examples package
# Copyright (c) 2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-examples

import urequests as requests # pylint: disable=import-error

class Map(object):

    def __init__(self, location):
        self.location = location
        self.zoom = 15

    def update(self, location):
        self.location = location

    def save(self, filename):
        file = open(filename, "wb")
        file.write(self.image)
        file.close()

    def zoom_in(self):
        self.zoom += 1

    def zoom_out(self):
        self.zoom -= 1

    def download(self):
        return requests.get(self.url)

    @property
    def image(self):
        image = self.download()
        return image.content

    @property
    def url(self):
        query = {
            "center": "%.8f,%.8f" % (self.location["lat"], self.location["lng"]),
            "markers": "%.8f,%.8f" % (self.location["lat"], self.location["lng"]),
            "size": "320x240",
            "zoom": self.zoom,
            "format": "jpg-baseline"
        }
        query_string = "&".join("%s=%s" % (key, value) for key, value in query.items())

        return "https://maps.googleapis.com/maps/api/staticmap?" + query_string

