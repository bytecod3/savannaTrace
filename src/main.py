# Author: Edwin Mwiti Maingi
# email: emwiti658@gmail.com
# This program creates a connection to emqx mqtt broker
# if the connection fails, it waits for 5 seconds and retries again
# it then gets tha IP address assigned from WIFI
# and finally publishes this IP address to a user subscribing to the same topic

# imports 
import paho.mqtt.client as mqtt
from time import sleep
import socket

# broker variables
broker = {
        "address": "broker.emqx.io",
        "port"   : 1883,
        "topic"  : "raspberry/ip_address",
	"retry_time": 5 # 5 seconds to retry connection
    }

def get_ip():
    ''' 
    This function uses sockets to find the local IP address of the Pi
    '''
    ip_address = ''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # try connect to a dummy IP
    sock.connect(("8.8.8.8", 80))
    ip_address = sock.getsockname()[0]
    
    #close socket connection
    sock.close()

    return ip_address


def  on_connection_callback(client, userdata, flags, response_code):
    '''
    This function will be called if we establish a connection to the broker 
    '''

    # debug the respose code
    print(f"[+] Connected with response code: {response_code}")

    # check if the connection was a succeess
    #while response_code != 0:
#	print(f"[-] Connection failed. Response code: {response_code}. Retrying in {broker['retry_time']} seconds")
#	sleep(broker['retry_time']) # wait for 5 seconds and retry

    # at this point we have a successful connection
    # publish the IP address message
    ip = get_ip()
    client.publish(broker["topic"], payload=ip, qos=0, retain=False)

    # debug
    print(f"[+] Published ip:{ip} to {broker['topic']}")
    


# create connection client
client = mqtt.Client()
client.on_connect = on_connection_callback
client.connect(broker["address"], broker["port"])

client.loop_forever()
