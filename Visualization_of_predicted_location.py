import serial
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

f = open("C:/Users/Taif/PycharmProjects/pythonProject1/data.txt", "r")
# Mapping of Preicted location to the coordinates inside the cylinder
def mapping(status):
    match status:
        case 0:
            return 7.0, 9.0
        case 1:
            return 7.0, 8.5
        case 2:
            return 7.0, 8.0
        case 3:
            return 7.0, 7.5
        case 4:
            return 7.0, 7.0
        case 5:
            return 7.0, 6.5
        case 6:
            return 7.0, 6.0
        case 7:
            return 7.5, 6.0
        case 8:
            return 7.5, 6.5
        case 9:
            return 7.5, 7.0
        case 10:
            return 7.5, 7.5
        case 11:
            return 7.5, 8.0
        case 12:
            return 7.5, 8.5
        case 13:
            return 7.5, 9.0
        case _:
            return 7.5, 7.5

#Inner radius of the cylinder
R1 = 5.2
#Outer radius of the disk
R2 = 0.8

fig = plt.figure()
ax = plt.axes(xlim=(0, 15), ylim=(0, 15))

sensor = plt.Circle((7.5, 7.5), R2, color='r', fill=True)
circle = plt.Circle((7.5, 7.5), R1, color='purple', fill=False)
ax.add_artist(circle)
ax.add_artist(sensor)

def animate(i):
    x, y = sensor.center

    if i == 0:
        return sensor
    else:
        data = []
        f.seek(0)
        data = f.readlines()
        print(data[0])
        mapped_vals = mapping(int(data[0]))
        x = mapped_vals[0]
        y = mapped_vals[1]
        print(x, y)
        sensor.center = (x, y)
        return sensor,

# Animation
anim = animation.FuncAnimation(fig, animate, frames=5, interval=200)
plt.axis('equal')
plt.legend(('Cylinder','Real sensor location'))
plt.title('Sensor Location')
plt.show()