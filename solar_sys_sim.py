import numpy as np
import matplotlib.pyplot as plt
import math
fig = plt.figure()
ax = plt.axes(projection='3d')

# Orbit function, with inputs:
# a = semi-major axis
# e = eccentricity
# Ω = longitude of ascending node
# i = inclination (to ecliptic)
# ω = argument of perihelion
# k = colour on graph
def orb(a,e,Ω,i,ω,k):
    # Lists of coordinates, which will contain points along the orbit:
    x = []
    y = []
    z = []

    # b = semi-minor axis:
    b = a * math.sqrt(1 - e**2)

    # c = linear eccentricity (distance from centre to focus):
    c = e * a

    # Converting orbital elements to radians:
    Ω *= np.pi/180
    i *= np.pi/180
    ω *= np.pi/180

    # Matrix transformations defining orientation of  orbit (based on Ω, i, ω):
    ω_mat = np.matrix([[np.cos(ω), np.sin(ω), 0],[-np.sin(ω), np.cos(ω), 0],[0, 0, 1]])
    i_mat = np.matrix([[1, 0, 0],[0, np.cos(i), np.sin(i)],[0, np.sin(-i), np.cos(i)]])
    Ω_mat = np.matrix([[np.cos(Ω), np.sin(Ω), 0],[-np.sin(Ω), np.cos(Ω), 0],[0, 0, 1]])
    
    # Calculating points along  orbit:
    for i in np.linspace(0,10,1000):
        # Vector representing points on sized orbit (based on a, b, c):
        orb_vec = np.matrix([[a * np.cos(i) - c],[b * np.sin(i) - c],[0]])

        # Vector representing points on transformed (oriented) orbit:
        trans_orb_vec = Ω_mat * i_mat * ω_mat * orb_vec

        # Appending elements of trans_orb_vec to respective coordinate lists:
        x.append(trans_orb_vec[0,0])
        y.append(trans_orb_vec[1,0])
        z.append(trans_orb_vec[2,0])
    
    ax.plot3D(x, y, z, color = k)

# Mercury:
orb(0.387, 0.206, 48.331, 7.005, 29.124, 'gray')

# Venus:
orb(0.723, 0.007, 76.680, 3.395, 54.884, 'magenta')

# Earth:
orb(1.000, 0.017, -11.261, 0.000, 114.208, 'cyan')

# Mars:
orb(1.524, 0.093, 49.558, 1.850, 286.502, 'red')

# Jupiter:
orb(5.204, 0.048, 100.464, 1.303, 273.867, 'black')

# Saturn:
orb(9.5826, 0.056, 113.665, 2.485, 339.392, 'yellow')

# Uranus:
orb(19.218, 0.047, 74.006, 0.773, 99.999, 'green')

# Neptune:
orb(30.11, 0.009, 131.784, 1.768, 276.336, 'blue')

# Scale of graph (± axis limits):
s = 1

plt.xlim(-s,s)
plt.ylim(-s,s)
ax.set_zlim(-s,s)
plt.show()