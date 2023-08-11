# savannaTrace
Raspberry MQTT Solution

## Problem statement
---

## Approach
---
I use the Raspberry Pi as the end device that will be used to publish messages to the broker.
The user device, either a laptop, smartphone or any othe device, will subscribe to the same topic that the Pi
publishes to.

The moment we connect the Pi to a WiFi network, we get the IP address, and save it into a message variable.
This variable is what we publish as a message to the raspberry/ip topic. 

The subscribed device can then get this IP address.
