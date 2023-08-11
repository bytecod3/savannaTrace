import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")

    client.subscribe("raspberry/ip_address")

# This function will be called when we receive a message
def on_message(client, userdata, message):
    print(f"{message.topic}, {message.payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# message to send if client is disconnected
client.will_set("raspberry/status", b'{"status": "OFF"}')

# create a connection
client.connect("broker.emqx.io", 1883, 60)

client.loop_forever()
