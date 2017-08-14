from network import WLAN
import urequests as requests
import machine
import time
TOKEN = "Assign_your_Ubidots_token_here" #Put here your TOKEN
DELAY = 1  # Delay in seconds
wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.INT_ANT)
# Assign your Wi-Fi credentials
wlan.connect("wifi-SSID-here", auth=(WLAN.WPA2, "wifi-password-here"), timeout=5000)
while not wlan.isconnected ():
    machine.idle()
print("Connected to Wifi\n")
# Builds the json to send the request
def build_json(variable1, value1, variable2, value2, variable3, value3):
    try:
        lat = 6.217
        lng = -75.567
        data = {variable1: {"value": value1},
                variable2: {"value": value2, "context": {"lat": lat, "lng": lng}},
                variable3: {"value": value3}}
        return data
    except:
        return None
# Sends the request. Please reference the REST API reference https://ubidots.com/docs/api/
def post_var(device, value1, value2, value3):
    try:
        url = "https://things.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json("fuel", value1, "position", value2, "speed", value3)
        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
       else:
           pass
    except:
        pass
while True:
    fuel = 123 # Data values
    speed = 234 # Data values
    post_var("pycom", fuel, 1, speed)
    time.sleep(DELAY)
