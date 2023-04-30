#!/usr/bin/env python3
import minimalmodbus
import time
ampti04 = minimalmodbus.Instrument('COM6', 1)  # port name, slave address (in decimal)

ampti04.serial.port                     # this is the serial port name
ampti04.serial.baudrate = 9600         # Baud
ampti04.serial.bytesize = 8
ampti04.serial.parity   = minimalmodbus.serial.PARITY_NONE
ampti04.serial.stopbits = 1
ampti04.serial.timeout  = 0.2          # seconds

ampti04.address                         # this is the slave address number
ampti04.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
ampti04.clear_buffers_before_each_transaction = True

ampti04.close_port_after_each_call = True
ampti04.clear_buffers_before_each_transaction = True

sleep_time=0.2

i=0
while i!=100:

    try:
        print("CH1:", ampti04.read_register(0,1,4)," C") #Read PT100 on channel 1
    except IOError:
        print("Failed to read CH1") 
    time.sleep(sleep_time) 
    
    try:
        print("CH2:", ampti04.read_register(1,1,4)," C") #Read PT100 on channel 2
    except IOError:
        print("Failed to read CH2") 
    time.sleep(sleep_time) 
    
    try:
        print("CH3:", ampti04.read_register(2,1,4)," C") #Read PT100 on channel 3
    except IOError:
        print("Failed to read CH3") 
    time.sleep(sleep_time) 
    
    try:
        print("CH4:", ampti04.read_register(3,1,4)," C") #Read PT100 on channel 4
    except IOError:
        print("Failed to read CH4") 
    time.sleep(sleep_time) 

    print("==========================")

    i+=1
   
ampti04.serial.close()
