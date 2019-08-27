import pygatt

adapter = pygatt.GATTToolBackend()

try:
	adapter.start()
