from pymodbus.client.sync import ModbusTcpClient
import time
modbus = ModbusTcpClient('localhost', port=5020)
address = 0

while True:
    response = modbus.read_holding_registers(address, 10)
    print response
    print response.registers
    time.sleep(2)
