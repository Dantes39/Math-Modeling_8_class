import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin
from matplotlib.animation import FuncAnimation

R = 1

fig, ax = plt.subplots()

anim_object, = plt.plot([],[],':')

xdata,ydata=[],[]

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

def updat(t):
    xdata.append(R*(cos(t)**3))
    ydata.append(R*(sin(t)**3))
    anim_object.set_data(xdata,ydata)

ani = FuncAnimation(fig,
                    updat, 
                    frames = np.arange(0,6*np.pi,0.1),
                    interval=50)

ani.save('animaca.1.gif')