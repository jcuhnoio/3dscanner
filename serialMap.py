import matplotlib.pyplot as plt
import numpy as np
import serial
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D
import warnings

warnings.filterwarnings('ignore')

# Sensor reading vs. Distance
calibrationplot = [[90,100,110,120,130,145,150,160,180,195,220,240,270,300,340,380,430,475,519],
                    [120,110,100,90,85,80,75,70,65,60,55,50,45,40,35,30,25,20,15]]

x = calibrationplot[0]
y = calibrationplot[1]

sensor2dist =  np.poly1d(np.polyfit(x, y,3)) # Fit curve to calibration plot

port = 'COM4' # For windows
# port = '/dev/tty.usbmodem21401' # For MAC

# Connect to Arduino
serialPort = serial.Serial(port = port, baudrate = 9600, timeout=1)

scanArray = []
scanning = True
scanpoints = 90 # Number of scans per sweep


print("Scanning in progress")
while scanning == True:
    scanArrayRow = []
    i = 0
    while i < scanpoints:
        data = serialPort.readline().decode().rstrip("\r\n")
        if len(data) > 0:
            if data == 'Scan complete':
                # print(data)
                scanning = False
            # elif len(data) > 0 and data != '\n':
            #     data = int(data)
                
            #     scanArrayRow.append(func(data,*list(popt[0])))
            # elif len(data) == 0:
            #    # print(type(data))
            #     i = i - 1
            else:
                try:
                    scanArrayRow.append(round(sensor2dist(int(data)),4))
                except ValueError:
                    i -= 1
        else:
            i -= 1
        i += 1
    scanArray.append(scanArrayRow)

# Last array ends up being [], remove it from dataset
scanArray.pop(-1)

# Flip rows where scanner is sweeping the opposite direction (every other row)
for i, row in enumerate(scanArray):
    if i%2 == 1:
        scanArray[i].reverse()

f = open("3dscanner/data.txt", "w")
f.write(str(scanArray))
f.close()
