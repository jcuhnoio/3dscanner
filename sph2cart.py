import numpy as np

def sph2cart(phi,theta,r):
    """
    Convert spherical coordinates to cartesian

    Args:
        phi: angle from x axis
        theta: angle from z axis
        r: radius
    
    Returns: 
        x: x position in cartesian
        y: y position in cartesian
        z: z position in cartesian
    """
    x = np.sin(theta)*np.cos(phi)*r
    y = np.sin(theta)*np.sin(phi)*r
    z = np.cos(theta)*r
    return (x,y,z)