import paho.mqtt.client as mqtt

# callback function
def on_connect_callback(client,userdata,flags, response_code):
    if response_code == 0:
        print("connected sucess");
    else:
        print(f"connection failed with code {response_code}")

client = mqtt.Client()
client.on_connect = on_connect_callback
client.connect("broker.emqx.io", 1883, 60);
client.loop_forever()
