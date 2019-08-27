from bluetooth import *

server_address = "DC:A6:32:0A:91:E4"
port = 1

sock = BluetoothSocket(RFCOMM)

sock.connect((server_address, port))

#count = 1
while True:
	message = input("Enter: ")
	if not message: break
	sock.send(message)
	data = sock.recv(1024)
	print("Recevied ", data)

sock.close()
