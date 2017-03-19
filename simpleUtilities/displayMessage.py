"""Display temperature and humidity in OLED."""
import ssd1306
from machine import I2C, Pin


class Display(object):
    """Display setup is here."""

    def __init__(self, sda=4, scl=5):
        """Initialize.

        sda => type(int)
        scl => type(int)
        """
        self.sda = sda
        self.scl = scl
        self.i2c = None
        self.display = None

    def configureI2C(self):
        """Configure the IO Pins here."""
        self.i2c = I2C(sda=Pin(self.sda), scl=Pin(self.scl))
        self.display = ssd1306.SSD1306_I2C(128, 64, self.i2c)
        self.display.fill(0)

    def displayMessageOnScreen(self, message="Hello", x=10, y=10):
        """Display the tesxt on the mentioned coordinates."""
        self.display.text(message, x, y)
        self.display.show()


if __name__ == "__main__":
    d = Display()
    d.configureI2C()
    d.displayMessage()
