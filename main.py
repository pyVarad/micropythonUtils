import network

def setupWirelessESP8266(ssid, password):
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.connect(ssid, password)

if __name__ == "__main__":
    setupWirelessESP8266('C-153', 'ayakkad@18')
