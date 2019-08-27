
import sys
import bluetooth

uuid = "8888"
#uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
service_matches = bluetooth.find_service(uuid=uuid)

if len(service_matches) == 0:
    print("couldn't find the FooBar service")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to ", name, " on ", host)

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((host, port))
sock.send("hello!!")
sock.close()


'''
from bluetooth import *

server_sock = BluetoothSocket(RFCOMM)
port = 1
server_sock.bind(("", port))
server_sock.listen(1)

uuid = "b6720f54-2c70-45a1-8787-b9b99b12b7e3"
advertise_service(sock = server_sock, name = "Foo Service", service_id=uuid)
client_sock.address = server_sock.accept()

data = server_sock.recv(1024)
client_sock.close()
server_sock.close() 	 	
'''
