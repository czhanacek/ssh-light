import paho.mqtt.client as mqtt
import os

def on_connect(client, userdata, flags, rc):
    print("Connected")

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    print("We got a message: " + str(msg.payload))

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

