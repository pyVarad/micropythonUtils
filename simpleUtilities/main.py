"""Main program is here to setup network."""
import dht
import machine
import time
from displayMessage import Display


def getTemperatureAndHumidity():
    """Main function to get temperature & humidity."""
    d = dht.DHT11(machine.Pin(16))
    d.measure()
    temp = d.temperature()
    humidity = d.humidity()
    return temp, humidity


if __name__ == "__main__":
    while True:
        temp, humidity = getTemperatureAndHumidity()
        show = Display(4, 5)
        show.configureI2C()
        show.displayMessageOnScreen("Temp:%d" % temp)
        show.displayMessageOnScreen("Humidity:%d" % humidity, 10, 20)
        show.displayMessageOnScreen("update in 5 sec.", 10, 30)
        time.sleep(5)
