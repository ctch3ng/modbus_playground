# modbus_playground
Control Modbus-RTU serial devices with Python minimalmodbus library

# Prerequisites
## Hardware 
+ Generic USB to RS485 adaptor
+ Waveshare Industrial Modbus RTU 8-ch Relay Module [Link](https://www.waveshare.com/modbus-rtu-relay.htm)
+ DFRobot URM14 - Industrial Ultrasonic Distance Sensor [Link](https://www.dfrobot.com/product-2173.html)

## Software 
+ Python>=3.9 - via Anaconda [Link](https://www.anaconda.com/products/distribution)
+ MinimalModbus [Link](https://minimalmodbus.readthedocs.io/en/stable/index.html)

Note: For Windows user, check your COM port settings under Device Manager. For Linux user, check your COM port settings under /dev/

# 02 Oct 2022 Updates
+ rtu_relay_read_info.py -- For reading registers' values from Waveshare Industrial Modbus RTU 8-ch Relay Module.
+ rtu_relay_control_demo.py -- For controlling the relays on the Waveshare Industrial Modbus RTU 8-ch Relay Module.

+ urm14_read_info.py --  For reading registers' values from URM14 - Industrial Ultrasonic Distance Sensor.
+ urm14_dist_read_loop.py -- For reading the distance register (100 times) from DFRobot URM14 - Industrial Ultrasonic Distance Sensor.
