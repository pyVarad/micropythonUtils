"""Simple LED On/Off."""
from machine import Pin
import time


def simpleLEDOn_Off(pin):
    """Turn On and Off Pin 2."""
    while True:
        pin_2 = Pin(2, Pin.OUT)
        pin_2.high()
        time.sleep(3)
        pin_2.low()
        time.sleep(3)


if __name__ == "__main__":
    simpleLEDOn_Off(pin=2)
