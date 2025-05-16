#!/usr/bin/python3

# incompartible interface
class EuropeanPlug:
    def voltage(self):
        return '230 volts from Europe socket'


# traget interface
class USAdapter:
    def get_power(self):
        pass
    
class Adapter(USAdapter):
    def __init__(self, europe_socket):
        self.europe_socket = europe_socket

    def get_power(self):
        return self.europe_socket.voltage()



def plugin(device: USAdapter):
    print(device.get_power())

europe_plug = EuropeanPlug()
adapter = Adapter(europe_plug)
plugin(adapter)

