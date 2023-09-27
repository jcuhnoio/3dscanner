import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = open("/Users/juno/Documents/PIE/3dscanner/data.txt", "r")
lst = f.read()
scanArray = json.loads(lst)[0:51]

phi = [np.deg2rad(ang) for ang in range(30,-31,-1)]
theta = [np.deg2rad(90-ang) for ang in range(30,-21,-1)]

print(len(phi),len(theta),len(scanArray))

def sph2car(phi,theta,r):
    x = np.sin(theta)*np.cos(phi)*r
    y = np.sin(theta)*np.sin(phi)*r
    z = np.cos(theta)*r
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
ax = plt.axes(projection='3d')
ax.scatter(xmat,ymat,zmat, c = xmat, s=1, cmap = 'ocean')

ax.set_xlim(-200,200)
ax.set_ylim(-200,200)
ax.set_zlim(0,200)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()