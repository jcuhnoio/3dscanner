import matplotlib.pyplot as plt
import numpy as np
import serial
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D

calibrationplot = [[15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 100, 110, 120],
                   [519, 475, 430, 380, 340, 300, 270, 240, 220, 195, 180, 160, 150, 145, 130, 120, 110, 100, 90]]



def func(x, a, b, c): # Define function shape to fit to
    return a * np.exp(-b * np.array(x)) + c

popt = curve_fit(func, calibrationplot[0], calibrationplot[1]) # Fit curve to calibration plot
popt = list(popt)

# func(x, *list(popt[0]))

serialPort = serial.Serial(port = '/dev/tty.usbmodem21401', baudrate = 9600, timeout=1)

scanArray = []
scanning = True
scanpoints = 90 # Number of scans per sweep

while scanning == True:
    scanArrayRow = []
    i = 0
    while i < scanpoints:
        data = serialPort.readline().decode()
        if data == 'Scan complete\r\n':
            # print(data)
            scanning = False
        elif len(data) > 0 and data != '\n':
            data = int(data)
            
            scanArrayRow.append(func(data,*list(popt[0])))
        elif len(data) == 0:
           # print(type(data))
            i = i - 1
        i += 1

    scanArray.append(scanArrayRow)

print(scanArray)

scanArray.pop(-1)

# Flip rows where scanner is sweeping the opposite direction (every other row)
for i, row in enumerate(scanArray):
    if i%2 == 1:
        scanArray[i].reverse()

print(scanArray)

phi = [ang for ang in range(45,-46,-1)]
theta = [ang for ang in range(60,-21,-1)]

def sph2car(phi,theta,r):
    x = np.cos(np.deg2rad(phi))*r
    y = np.sin(np.deg2rad(phi))*r
    z = np.sin(np.deg2rad(theta))*r
    return (x,y,z)

xmat = []
ymat = []
zmat = []

for rowIndex, row in enumerate(scanArray):
    currentTheta = theta[rowIndex]
    for columnIndex, value in enumerate(row):
        currentPhi = phi[columnIndex]
        x,y,z = sph2car(currentPhi,currentTheta,value)
        xmat.append(x)
        ymat.append(y)
        zmat.append(z)


    
fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(ymat,xmat,zmat,s=1)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
