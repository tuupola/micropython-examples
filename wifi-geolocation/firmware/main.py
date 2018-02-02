import ubinascii as binascii # pylint: disable=import-error
import urequests as requests # pylint: disable=import-error
import ujson as json # pylint: disable=import-error
import ustruct as struct # pylint: disable=import-error
import network # pylint: disable=import-error

with open("settings.json") as fp:
    settings = json.loads(fp.read())

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(settings["wifi"]["username"], settings["wifi"]["password"])

while not station.isconnected():
    pass

data = {
    "considerIp": False,
    "wifiAccessPoints": []
}

networks = station.scan()
for wifi in networks:
    entry = {
        "ssid": wifi[0],
        "macAddress": "%02x:%02x:%02x:%02x:%02x:%02x" % struct.unpack("BBBBBB", wifi[1]),
        "signalStrength": wifi[3],
        "channel": wifi[2]
    }
    data["wifiAccessPoints"].append(entry)

headers = {"Content-Type": "application/json"}
url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + settings["api_key"]

response = requests.post(url, headers=headers, data=json.dumps(data))
location = json.loads(response.content)["location"]

query = {
    "center": "%.8f,%.8f" % (location["lat"], location["lng"]),
    "markers": "%.8f,%.8f" % (location["lat"], location["lng"]),
    "size": "320x200",
    "zoom": 12,
    "format": "jpg"
}
query_string = "&".join("%s=%s" % (key, value) for key, value in query.items())

url = "https://maps.googleapis.com/maps/api/staticmap?" + query_string

print(url)