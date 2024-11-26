import numpy as np
import matplotlib.pyplot as plt

#define the constants we need to use
sigma = 10
r_c = 28
b_c = 8/3

#define the vector r
def f(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sigma*(y-x)
    fy = r_c*x-y-x*z
    fz = x*y-b_c*z
    return np.array([fx,fy,fz],float)

#define the time range
a = 0.0
b = 50.0
N = 10000
dt = (b-a)/N

#define time steps
tpoints = np.arange(a,b,dt)
xpoints = []
ypoints = []
zpoints = []

#define initial conditions
r = np.array([0.0,1.0,0.0],float)

#start iteration
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    k1 = dt*f(r,t)
    k2 = dt*f(r+0.5*k1,t+0.5*dt)
    k3 = dt*f(r+0.5*k2,t+0.5*dt)
    k4 = dt*f(r+k3,t+dt)
    r += (k1+2*k2+2*k3+k4)/6

#plt.plot(tpoints,xpoints)
plt.plot(tpoints,ypoints)
plt.xlabel("time (s)")
plt.ylabel("y (unit)")
plt.title("value of y with respect to time")
plt.show()

plt.plot(xpoints,zpoints)
plt.xlabel("x (unit)")
plt.ylabel("z (unit)")
plt.title("z against x")
plt.show()

