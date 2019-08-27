from gattlib import DiscoveryService, BeaconService

service =DiscoveryService("Automatic Lights")
devices = service.discover(1)

for addr, name in devices.items():
	print("name: {}, addr : {}".format(name, addr)) 


print(devices)

service = BeaconService()
x = service.scan(15)
print(x)
