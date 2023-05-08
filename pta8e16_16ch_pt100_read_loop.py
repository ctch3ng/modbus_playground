#!/usr/bin/env python3
import minimalmodbus
import time
pta8e16 = minimalmodbus.Instrument('COM3', 1)  # port name, slave address (in decimal)

pta8e16.serial.port                     # this is the serial port name
pta8e16.serial.baudrate = 9600         # Baud
pta8e16.serial.bytesize = 8
pta8e16.serial.parity   = minimalmodbus.serial.PARITY_NONE
pta8e16.serial.stopbits = 1
pta8e16.serial.timeout  = 0.2          # seconds

pta8e16.address                         # this is the slave address number
pta8e16.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
pta8e16.clear_buffers_before_each_transaction = True

pta8e16.close_port_after_each_call = True
pta8e16.clear_buffers_before_each_transaction = True

sleep_time=0.2

i=0
while i!=100:
    j=0;
    while j!=16:
        try:
            print("CH",j+1,":", pta8e16.read_register(j,1,3)," C") #Read PT100 on channel 1, memory address 0, 1 decimal place, control code 4
        except IOError:
            print("Failed to read CH",j+1) 
        time.sleep(sleep_time) 
        print("==========================")
        j+=1
    i+=1
   
pta8e16.serial.close()
