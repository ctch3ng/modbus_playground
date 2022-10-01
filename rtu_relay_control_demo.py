#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3
import minimalmodbus
import time

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

relay_status = [1,0,0,0,0,0,0,0]

#Turn on the relay one by one
for i in range(len(relay_status)):
    relay_status.append(relay_status.pop(0)) #shift relay_status by 1 bit
    try:
        print("W States of Relays:",relay_status, rtu_relay.write_bits(0,relay_status)) #Write States of Relays 
    except IOError:
        print("Failed to write States of Relays")   
    time.sleep(0.03)
    try:
        print("R States of Relays:", rtu_relay.read_bits(0,8,1)) #Read States of Relays 
    except IOError:
        print("Failed to read States of Relays")

#Turn off all the relay 
try:
    print("W States of Relays:",[0,0,0,0,0,0,0,0], rtu_relay.write_bits(0,[0,0,0,0,0,0,0,0])) #Write States of Relays 
except IOError:
    print("Failed to write States of Relays")
try:
    print("R States of Relays:", rtu_relay.read_bits(0,8,1)) #Read States of Relays 
except IOError:
    print("Failed to read States of Relays")
rtu_relay.serial.close()


# In[ ]:





# In[ ]:




