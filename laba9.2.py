import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0,10,0.1)
def dengi(n,t):
    dndt = -k*n*t
    return dndt

k = 0.08

n_0 = 1000

invest = odeint(dengi, n_0, t)
plt.plot(t, invest, label = "инвестиции в Зимбибве")
plt.title('инвестиции в Зимбибве')
plt.xlabel('время в годах')
plt.ylabel('$')
plt.show()
     