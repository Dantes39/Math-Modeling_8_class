import matplotlib.pyplot as plt
import numpy as np
from numpy import cos,sin
R=3
x=R*(t-sin(t))
y=R*(1-cos(t))
t = np.arange(-2*np.pi,2*np.pi,0.1)
plt.plot(x,y,color='g',marker='.',ms= 5)
plt.plot(x,y,linestyle='--',linewidth= 5)
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.axis('equal')
plt.show