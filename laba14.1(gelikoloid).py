import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)

a = 2
b = 6
c = 4
h = 12
l = 3
m = 7
n = 5

phi = np.linspace(-2 * np.pi, 2 * np.pi, 100)
theta = np.linspace(-2 * np.pi, 2 * np.pi, 100)

x = np.outer(phi, np.cos(theta)) + l*np.outer(np.ones(np.size(phi)), (theta)**2 )
y = np.outer(phi, np.sin(theta)) + m*np.outer(np.ones(np.size(phi)), theta **2)
z = n*np.outer(np.ones(np.size(phi)), theta **2)

ax.plot_surface(x, y, z, color='r')
plt.show()