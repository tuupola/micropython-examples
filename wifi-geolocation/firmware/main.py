import ubinascii as binascii # pylint: disable=import-error
import urequests as requests # pylint: disable=import-error
import ujson as json # pylint: disable=import-error
import ustruct as struct # pylint: disable=import-error
import network # pylint: disable=import-error
import display # pylint: disable=import-error
import m5stack # pylint: disable=import-error

with open("settings.json") as fp:
    settings = json.loads(fp.read())

print("Connecting to wifi.")

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(settings["wifi"]["username"], settings["wifi"]["password"])

while not station.isconnected():
    pass


data = {
    "considerIp": False,
    "wifiAccessPoints": []
}

print("Scanning networks.")

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

print("Locating.")

response = requests.post(url, headers=headers, data=json.dumps(data))
location = json.loads(response.content)["location"]

query = {
    "center": "%.8f,%.8f" % (location["lat"], location["lng"]),
    "markers": "%.8f,%.8f" % (location["lat"], location["lng"]),
    "size": "320x240",
    "zoom": 15,
    "format": "jpg-baseline"
}
query_string = "&".join("%s=%s" % (key, value) for key, value in query.items())

print("Downloading map.")

url = "https://maps.googleapis.com/maps/api/staticmap?" + query_string
image = requests.get(url)

file = open("/flash/map.jpg", "wb")
file.write(image.content)
file.close()

tft = display.TFT()
tft.init(
    tft.ILI9341,
    spihost=tft.HSPI,
    width=320,
    height=240,
    mosi=m5stack.TFT_MOSI_PIN,
    miso=m5stack.TFT_MISO_PIN,
    clk=m5stack.TFT_CLK_PIN,
    cs=m5stack.TFT_CS_PIN,
    dc=m5stack.TFT_DC_PIN,
    rst_pin=m5stack.TFT_RST_PIN,
    backl_pin=m5stack.TFT_LED_PIN,
    backl_on=1,
    speed=2600000,
    invrot=3,
    bgr=True
)

tft.orient(tft.LANDSCAPE)
tft.font(tft.FONT_Small, fixedwidth=True)
tft.image(0, 0, "/flash/map.jpg")

print("Done!")
print(url)