import paho.mqtt.client as mqtt
from time import sleep
from bluetooth import *
global flag
flag = True

def start_client(broker='192.168.2.45', sub_list=['other', 'info'], client_name='client-002'):
    return broker, sub_list, mqtt.Client(client_name)

broker, sub_list, client = start_client()

pub_topic = sub_list[0]
sub_topic = sub_list[1]



def on_message(client, userdata, message):
    sleep(1)
    message = str(message.payload.decode("utf-8").strip())
    print("recived message, ", message)
    client.publish(pub_topic, "This is the pi")
    
def on_connect(client, userdata, flags, rc):
    sleep(1)
    print(client._client_id, " has connected ", rc, "flags are ", flags)

def on_disconnect(client, userdata, rc):
    sleep(1)
    print(client._client_id, " has diconnected ", rc)

client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.connect(broker)
client.loop_start()

sleep(1)

print("listening on ", sub_topic)
client.subscribe(sub_topic)

print("returning info on ", pub_topic)
while flag:
    sleep(1)

print("Closing Client")
sleep(1)
client.disconnect()
client.loop_stop()
