import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0,10,0.1)

m = 15

def ne_ponayt(v,t):
    dvdt = (F-k*v**2)/m
    return dvdt

v = 12

k = 0.08

v_0 = 0

F = 150

zakon = odeint(ne_ponayt, v_0, t)
plt.plot(t, zakon, label = "бег в воде xD")
plt.title('бег в воде xD')
plt.xlabel('время t')
plt.ylabel('скорость V')
plt.show()
     