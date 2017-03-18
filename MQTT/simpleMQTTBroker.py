"""MQTT Broker."""

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    """Subscribe to home on successful connection."""
    print("Connected with result code "+str(rc))
    client.subscribe("home/#")


def on_message(client, userdata, msg):
    """Get the messages from the client."""
    print(msg.topic+" "+str(msg.payload))


if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("192.168.5.7", 1883, 60)
    client.loop_forever()
