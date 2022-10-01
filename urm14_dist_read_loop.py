#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python3
import minimalmodbus
import time
urm14 = minimalmodbus.Instrument('COM6', 12)  # port name, slave address (in decimal)

urm14.serial.port                     # this is the serial port name
urm14.serial.baudrate = 19200         # Baud
urm14.serial.bytesize = 8
urm14.serial.parity   = minimalmodbus.serial.PARITY_NONE
urm14.serial.stopbits = 1
urm14.serial.timeout  = 0.2          # seconds

urm14.address                         # this is the slave address number
urm14.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
urm14.clear_buffers_before_each_transaction = True

urm14.close_port_after_each_call = True
urm14.clear_buffers_before_each_transaction = True

sleep_time=0.2

i=0
while i!=100:
       
    try:
        urm14.write_register(8,8,0,6)
        #print("Control register:", urm14.write_register(8,8,0,6)) #Write Control register
    except IOError:
        pass   
    time.sleep(sleep_time)    

    try:
        print("Distance register:", urm14.read_register(5,1,3)," mm") #Read Distance register
    except IOError:
        pass

    i+=1
   
urm14.serial.close()


# In[ ]:




