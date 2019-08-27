from bluetooth import  *
sock = BluetoothSocket(RFCOMM)
server_address = "DC:A6:32:0A:91:E4"
port = 1
sock.connect((server_address,port))
sock.close()
