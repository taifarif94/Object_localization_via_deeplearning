import serial
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


#Inner radius of the cylinder
R1 = 5.2
#Outer radius of the disk
R2 = 0.8

iteration = 0


#Baudrate
baudrate1 = 9600
#COM Port
port1 = 'COM2'  # set the correct port before run it

f = open("data.txt", "w+")

for i in range(5):
    f.write('5')
    f.write("\n")
    f.flush()

serial1 = serial.Serial(port=port1, baudrate=baudrate1)
serial1.timeout = 2  # set read timeout
# print serial1  # debug serial.
print(serial1.is_open)  # True for opened
if serial1.is_open:
    while True:
        size = serial1.inWaiting()
        if size:
            data = serial1.read(size)
            f.seek(0)
            f.write((chr(int.from_bytes(data, "little"))))
            f.write("\n")
            f.flush()
            print(data)
        else:
            print('no data')
        time.sleep(1)
else:
    print('serial1 is closed')
serial1.close()  # close serial1 if serial1 is open.