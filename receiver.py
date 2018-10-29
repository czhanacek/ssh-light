import paho.mqtt.client as mqtt
import os
from flasher import LED_Light


led = LED_Light()
def on_connect(client, userdata, flags, rc):
    print("Connected")

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    if(msg.payload == "connection"):
        led.flash()
    

def main():
    
    client = mqtt.Client("laptop")
    client.on_connect = on_connect
    client.on_message = on_message

    hostname = os.environ["MQTT_SERVER"]

    client.connect(hostname, 1883, 60)

    client.subscribe("ssh_connections", 0)
    client.loop_forever()

if __name__ == "__main__":
    main()

