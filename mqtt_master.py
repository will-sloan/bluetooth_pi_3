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

def bluetooth_call(message):
	server_address = "DC:A6:32:0A:91:E4"
	port = 1

	sock = BluetoothSocket(RFCOMM)

	sock.connect((server_address, port))
	sock.send(message)
	#sleep(3)
	data = sock.recv(1024)
	if not data: 
		return "Nothing"
	
	return bytes.decode(data)


def on_message(client, userdata, message):
    sleep(1)
    message = str(message.payload.decode("utf-8").strip())
    
    try:
        if message == "quit":
            print("setting flag to false")
            global flag
            flag = False
        elif message == "light":
            print("getting light")
            client.publish(pub_topic, bluetooth_call(message) + "\n")
        elif message == "temp":
            print("getting temp")
            client.publish(pub_topic, bluetooth_call(message) + "\n")
        else:
            client.publish(pub_topic, bluetooth_call(message) + " was recived on pi\n")
    except Exception as err:
        print(err)
    finally:
        print("Messsage recieved: ", message, "\n")

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

print("Closing Temp/Light Client")
sleep(1)
client.disconnect()
client.loop_stop()
