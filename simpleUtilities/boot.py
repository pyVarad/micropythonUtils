"""Boot file."""
import gc
import network


def setupWirelessESP8266(ssid, password):
    """Setup wireless."""
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.connect(ssid, password)


if __name__ == "__main__":
    gc.collect()
    setupWirelessESP8266('C-153', 'ayakkad@18')
