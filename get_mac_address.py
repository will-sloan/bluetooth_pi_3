from gattlib import GATTRequester, DiscoveryService
service =DiscoveryService()
devices = service.discover(2)
address = None
for addr, name in devices.items():
	if "CA" in addr:
		address = addr
	
print(address)

req = GATTRequester(address)
try:
	name = req.read_by_uuid('8888')[0]
	print("uuid name ", name)
except:
	print("not uuid")
	
try: 
	name = req.read_by_handle('8888')[0]
	print("handle name ", name)
except:
	print("not handle")
print(req)

print(name)
