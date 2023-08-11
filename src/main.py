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

# imports for OLED
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# ===================== OLED ==========================
RST = 24

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()
# Load default font.
font = ImageFont.load_default()


# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)


# ========================= END OF OLED ==========================

# broker variables
broker = {
        "address": "broker.emqx.io",
        "port"   : 1883,
        "topic"  : "raspberry/ip_address",
        "retry_time": 5 # 5 seconds to retry connection
    }

# initialize display
RST = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

def update_display(message):
    '''
    Display the IP address on an SSD1306 OLED
    '''
    draw.text((5, 0), "Network Stats", font=font, fill=255)
    draw.text((5, 15),"IP: " + str(message),  font=font, fill=255)
    disp.image(image)
    disp.display()
    
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
    
    update_display(str(ip))

    # debug
    print(f"[+] Published ip:{ip} to {broker['topic']}")
    
# create connection client
client = mqtt.Client()
client.on_connect = on_connection_callback
client.connect(broker["address"], broker["port"])

client.loop_forever()
