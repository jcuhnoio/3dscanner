import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sph2cart import sph2cart

# f = open("/Users/juno/Documents/PIE/3dscanner/data.txt", "r")
f = open("3dscanner/data.txt","r")
lst = f.read()
scanArray = json.loads(lst)[0:51]

# Pan angle
phi = [np.deg2rad(ang) for ang in range(30,-31,-1)]
# Tilt angle
theta = [np.deg2rad(90-ang) for ang in range(30,-21,-1)]

# Array for storing x coordinates
xmat = []
ymat = []
zmat = []

# Convert spherical to cartesian
for rowIndex, row in enumerate(scanArray):
    currentTheta = theta[rowIndex]
    for columnIndex, value in enumerate(row):
        currentPhi = phi[columnIndex]
        x,y,z = sph2cart(currentPhi,currentTheta,value)
        xmat.append(x)
        ymat.append(y)
        zmat.append(z)

# Plot 3D point cloud
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