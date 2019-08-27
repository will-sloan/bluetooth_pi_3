from bluetooth import *

server_address = "DC:A6:32:0A:91:E4"
port = 1
global flag
flag = True

sock = BluetoothSocket(RFCOMM)

sock.connect((server_address, port))


while flag:
	message = input("What to send: ")
	
	try:
		sock.send(message)
		if message == 'quit': break
		data = sock.recv(1024)
		if not data: continue
		print(bytes.decode(data))
	except Exception as err:
		print("Connection Failed ", err)
		receive = False
	
sock.close()
