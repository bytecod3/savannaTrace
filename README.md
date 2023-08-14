# savannaTrace
Raspberry MQTT Solution

## Problem statement
---

## Approach
---
I use the Raspberry Pi as the end device that will be used to publish messages to the broker.
The user device, either a laptop, smartphone or any other device, will subscribe to the same topic that the Pi
publishes to.

The moment we connect the Pi to a WiFi network, we get the IP address, and save it into a message variable.
This variable is what we publish as a message to the raspberry/ip topic. 

The subscribed device can then get this IP address.

Based on the problem statement, the parameters used are as follows:
1. Broker: broker.emqx.io
2. Port: 1883
3. Topic: raspberry/ip_address

## Program flowchart
---
![Savanna trace flowchart](./tests/savanna-trace-flowchart.png)

The code for this is in the ```c src/main.py ```  file.

## Tests
---
I used a Raspberry Pi model 4B and the open source MQTTX application to perform tests. Below are the screenshots of these tests.

### Raspberry Pi terminal publishing the IP address
![Raspberry Pi](./tests/raspberry-pi-pub-mqttx.png)

### MQTTX application receiving message
![Raspberry Pi](./tests/ip-address-mqttx.png)

### Demonstration
I built a quick prototype to test the hardware. I used an I2C OLED screen to display the IP address. Below are the screenshots
---
Same IP address displaying on the OLED screen
![Raspberry Pi](./tests/protoboard.jpg)

![Raspberry Pi](./tests/protoboard-pi.jpg)
