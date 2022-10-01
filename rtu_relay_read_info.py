#!/usr/bin/env python3
import minimalmodbus

rtu_relay = minimalmodbus.Instrument('COM6', 1)  # port name, slave address (in decimal)

rtu_relay.serial.port                     # this is the serial port name
rtu_relay.serial.baudrate = 9600         # Baud
rtu_relay.serial.bytesize = 8
rtu_relay.serial.parity   = minimalmodbus.serial.PARITY_NONE
rtu_relay.serial.stopbits = 1
rtu_relay.serial.timeout  = 0.05          # seconds

rtu_relay.address                         # this is the slave address number
rtu_relay.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
rtu_relay.clear_buffers_before_each_transaction = True

rtu_relay.close_port_after_each_call = True
rtu_relay.clear_buffers_before_each_transaction = True

try:
    print("States of Relays:", rtu_relay.read_bits(0,8,1)) #Read States of Relays 
except IOError:
    print("Failed to read States of Relays")

try:
    print("Device Address:", rtu_relay.read_registers(0x4000,1,3)) #Read States of Relays 
except IOError:
    print("Failed to read Device Address Command") 
    
rtu_relay.debug = True
try:
    print("Software Version:", rtu_relay.read_registers(0x8000,1,3)) #Read Software Version
except IOError:
    print("Software Version can only be read in debug mode as the reply is not in standard format")  

rtu_relay.serial.close()
