"""Temperature sensor."""
import machine
import time
import webrepl
import ubinascii
from temperatureSensor import temperatureAndHumidity

from umqtt.simple import MQTTClient

CONFIG = {
    "broker": "192.168.5.7",
    "sensor_pin": 4,
    "client_id": b"esp8266_" + ubinascii.hexlify(machine.unique_id()),
    "topic": b"home",
}

client = None
sensor_pin = None


def setup_pins():
    """Set the pins from which the data will be fetched."""
    global sensor_pin
    sensor_pin = machine.Pin(CONFIG['sensor_pin'], machine.Pin.IN)


def load_config():
    """Get the configurations from config.json."""
    import ujson as json
    try:
        with open("/config.json") as f:
            config = json.loads(f.read())
    except (OSError, ValueError):
        print("Couldn't load /config.json")
        save_config()
    else:
        CONFIG.update(config)
        print("Loaded config from /config.json")


def save_config():
    """Save the config json for the first time."""
    import ujson as json
    try:
        with open("/config.json", "w") as f:
            f.write(json.dumps(CONFIG))
    except OSError:
        print("Couldn't save /config.json")


def main():
    """Main program starts here."""
    client = MQTTClient(CONFIG['client_id'], CONFIG['broker'])
    client.connect()
    temp, humidity = temperatureAndHumidity()
    print("Connected to {}".format(CONFIG['broker']))
    while True:
        data = sensor_pin.value()
        client.publish(
            '{}/{}'.format(
                        CONFIG['topic'],
                        CONFIG['client_id']
                        ), bytes(str(data), 'utf-8')
                    )
        print('Sensor state: {}'.format(data))
        time.sleep(5)


if __name__ == '__main__':
    load_config()
    setup_pins()
    main()
