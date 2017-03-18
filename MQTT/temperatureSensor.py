"""Sense the temperature."""

import dht
import machine


def temperatureAndHumidity():
    """Main program starts here."""
    d = dht.DHT11(machine.Pin(16))
    d.measure()
    temp = d.temperature()
    humidity = d.humidity()
    return temp, humidity
