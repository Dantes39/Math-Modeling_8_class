import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np

fig = plt.figure()

def circle_func(x_c_p, y_c_p, R, N):
    cycl_x = np.zeros(N)
    cycl_y = np.zeros(N)
    
    for i in range(N):
        alpha = np.linspace(0, 2*np.pi, 10)
        cycl_x[i] = x_c_p + alpha
        cycl_y[i] = y_c_p 
    return x, y

a = 1
b = 3
c = 2

x = np.linspace(-5, 5, 100)
y = a*x**2+b*x+c
N = 100
R=5


anim_list = []

for i in range(N):
    x, y = circle_func(x[i], y[i], N=N, R=R)
    circle, = plt.plot(x, y, '-')
    anim_list.append([circle])
    
ani = ArtistAnimation(fig, anim_list, interval=50)
ani.save('pocherk_lexi.gif')

    
    
    



    
    