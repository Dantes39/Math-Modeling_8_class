import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0,100,0.1)
def baktery(n,t):
    dndt = k*n
    return dndt

k = 0.05

n_0 = 1

razmo = odeint(baktery, n_0, t)
plt.plot(t, razmo, label = "кол-во бактерий на экране смартфона")
plt.title('кол-во бактерий на экране смартфона')
plt.show()
     