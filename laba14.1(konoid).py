import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

N = 100
alpha = np.linspace(0, 10, N)

x = np.cos(alpha)
y = np.sin(alpha)
z = alpha * 0.1

a = 2
b = 6
c = 4
h = 12
l = 3
m = 7
n = 5

phi = np.linspace(-2 * np.pi, 2 * np.pi, 100)
theta = np.linspace(-2 * np.pi, 2 * np.pi, 100)

xl = np.outer(phi, np.cos(theta)) 
yl = np.outer(phi, np.sin(theta)) 
zl = h*np.outer(np.ones(np.size(phi)), theta)

ball, = ax.plot(x, y, z, 'o', color='r')
line, = ax.plot(x, y, z, '-', color='r')

def animation_func(i):
    ball.set_data(x[i],y[i])
    ball.set_3d_properties(z[i])
    
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])
    
ax.set_xlim3d([-1.0, 1.0])
ax.set_xlabel('lexa')

ax.set_ylim3d([-1.0, 1.0])
ax.set_ylabel('lox')

ax.set_zlim3d([-1.0, 1.0])
ax.set_zlabel('shutka')


ani = animation.FuncAnimation(fig, animation_func, N, interval= 10)

plt.show()

ani.save("xz,hto_eto.gif")