import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

    # publish a message
    for i in range(5):
        client.publish('raspberry/ip', payload=i, qos=0, retain=False)
        print(f"send {i} to raspberry/ip")


client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

client.loop_forever()
