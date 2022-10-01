#!/usr/bin/env python
# coding: utf-8

# In[110]:


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

try:
    print("Module PID Register:", urm14.read_register(0,0,3)) #Read Module PID Register
except IOError:
    print("Failed to read Module PID Register")
time.sleep(sleep_time)    
    
try:
    print("Module VID Register:", urm14.read_register(1,0,3)) #Read Module VID Register
except IOError:
    print("Failed to read Module VID Register")
time.sleep(sleep_time)    
    
try:
    print("Module Address Register:", urm14.read_register(2,0,3)) #Read Module Address Register
except IOError:
    print("Failed to read Module Address Register")
time.sleep(sleep_time)    
   
try:
    print("Serial parameter control register 1:", urm14.read_register(3,0,3)) #Read Serial parameter control register 1
except IOError:
    print("Failed to read Serial parameter control register 1")
time.sleep(sleep_time)    
    
try:
    print("Serial parameter control register 2:", urm14.read_register(4,0,3)) #Read Serial parameter control register 2
except IOError:
    print("Failed to read Serial parameter control register 2")
time.sleep(sleep_time)    
       
try:
    print("Onboard temperature data register:", urm14.read_register(6,0,3)) #Read Onboard temperature data register
except IOError:
    print("Failed to read Onboard temperature data register")
time.sleep(sleep_time)    
        
try:
    print("External temperature compensation data register:", urm14.read_register(7,0,3)) #Read External temperature compensation data register
except IOError:
    print("Failed to read External temperature compensation data register")
time.sleep(sleep_time)    
        
try:
    print("Control register:", urm14.read_register(8,0,3)) #Read Control register
except IOError:
    print("Failed to read Control register")
time.sleep(sleep_time)    
       
try:
    print("Electrical noise level register:", urm14.read_register(9,0,3)) #Read Electrical noise level register
except IOError:
    print("Failed to read Electrical noise level register")
time.sleep(sleep_time)    
       
try:
    print("Control register:", urm14.write_register(8,8,0,6)) #Write Control register
except IOError:
    print("Failed to write Control register")    
time.sleep(sleep_time)    
   
try:
    print("Distance register:", urm14.read_register(5,1,3)," mm") #Read Distance register
except IOError:
    print("Failed to read Distance register")

urm14.serial.close()


# In[ ]:




