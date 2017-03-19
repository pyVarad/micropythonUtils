"""Test simple display."""
import dht
import machine
from displayMessage import Display
from utime import localtime


def main():
    """Main function to get temperature & humidity."""
    d = dht.DHT11(machine.Pin(16))
    d.measure()
    temp = d.temperature()
    humidity = d.humidity()
    return temp, humidity


if __name__ == "__main__":
    temp, humidity = main()
    print(temp, humidity)
    show = Display(4, 5)
    show.configureI2C()
    show.displayMessageOnScreen("Temp:%d" % temp)
    show.displayMessageOnScreen("Humidity:%d" % humidity, 20, 20)
    dt = localtime()
