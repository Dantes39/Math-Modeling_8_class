import matplotlib.pyplot as plt
import numpy as np
from numpy import cos,sin
R=3
t = np.arange(-2*np.pi,2*np.pi,0.1)
x=R*(cos(t)**3)
y=R*(sin(t)**3)
plt.plot(x,y,color='g',marker='p',ms= 10)
plt.plot(x,y,linestyle=':',linewidth= 5)
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.axis('equal')
plt.show