import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation

R = 1

fig, ax = plt.subplots()

anim_object, = plt.plot([],[],'-')

xdata,ydata=[],[]

ax.set_xlim(0, 4*np.pi)
ax.set_ylim(-2, 2)

def updat(t):
    xdata.append(R*(cos(t)**3))
    ydata.append(R*(sin(t)**3))
    anim_object.set_data(xdata,ydata)

ani = FuncAnimation(fig,
                    updat, 
                    frames = np.arange(0,4*np.pi,0.1),
                    interval=50)

ani.save('animaca.gif')