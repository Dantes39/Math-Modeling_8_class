import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 20, 0.01)

def diff_func(z, t):
    y, x = z
    dy_dt = x
    dx_dt = -np.sin(y)*x-5 - 3 * y * t
    return dy_dt,dx_dt
y0 = 0.01
x0 = 0.05
z0 = y0,x0
sol = odeint(diff_func,z0,t)
plt.plot(sol[:,1],sol[:,0],'b')

