import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


G = 6.67 * 10**(-11)
sun_mass = 1.9 * 10**30

seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day =  24 * 60 * 60
years = 2
t = np.arange(0, years*seconds_in_year, seconds_in_day)

def grav_func(z, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2) = z
    dxdt1 = v_x1
    dv_xdt1 = -G * sun_mass * x1 / (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = -G * sun_mass * y1 / (x1**2 + y1**2)**1.5
    
    dxdt2 = v_x2
    dv_xdt2 = -G * sun_mass * x2 / (x2**2 + y2**2)**1.5
    dydt2 = v_y2
    dv_ydt2 = -G * sun_mass * y2 / (x2**2 + y2**2)**1.5
    
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2)


x01 = 149000000000.0
v_x01 = 0.0
y01 = 0.0
v_y01 = -29163.96599832879

x02 = 149000000000.0
v_x02 = 0.0
y02 = 0.0
v_y02 = -29163.96599832879

z0 = (x01, v_x01, y01, v_y01,
      x02, v_x02, y02, v_y02)

sol = odeint(grav_func, z0, t)

fig = plt.figure()
planets = []

for i in range(0, len(t), 1):
    sun,= plt.plot([0], [0], 'yo', ms=10)
    p1, = plt.plot(sol[i, 0], sol[i, 2], 'o', color='b')
    planets.append([p1])
    
ani = ArtistAnimation(fig, planets, interval=50)
plt.axis('equal')
ani.save('earth.gif')
    
#def tochechki (r, N, v):
#    for i in range (0, N, 1):
#        al = 2*np.pi/N
#        x = np.cos(al * i) * r
#        y = np.sin(al * i) * r
#        if x<0 and y<0:
#            vx = v*np.cos(0.5*np.pi-al*i)
#            vy= -v*np.sin(0.5*np.pi-al*i)
#        elif x<0 and y>0:
#            vx = v*np.sin(al*i)
#            vy = -v*np.cos(al*i)
#        elif x>0 and y>0:
#            vx = v*np.sin(al*i)
#            vy = -v*np.cos(al*i)
#        elif x>0 and y<0:
#            vx = v*np.cos(0.5*np.pi-al*i)
#            vy= -v*np.sin(0.5*np.pi-al*i)
#        else:
#            vx = 0
#            vy = 0
#            plt.plot(0, 0, marker="o",)  
#        print(x, y, vx, vy)
#        plt.arrow(x, y, vx, vy)
#        plt.plot(x, y, marker="o")  
#    plt.axis("equal")
#    plt.plot(x = 0, y = 0, marker="o",)  
#    plt.show()
#
#tochechki (1, 15, 1)