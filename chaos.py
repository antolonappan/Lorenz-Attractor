import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

rho =28.
sigma =10.
beta = 8./3
t = np.arange(0,100,.01)
x0=1
y0=1
z0=1

def coupled(w, r, v):

    x, y, z = w
    raw, si,beta = v
    f = [sigma*(y-x),x*(rho-z)-y,x*y-beta*z ]
    return f




v = [rho,sigma,beta]
w0 =[x0,y0,z0]

wsol = odeint(coupled, w0, t, args=(v,))

with open('cha', 'w') as f:
    
    for t1, w1 in zip(t, wsol):
        print >> f, t1, w1[0], w1[1],w1[2]

t, x, y, z = loadtxt('cha', unpack=True)



x0=1+1e-9
y0=1
z0=1

def coupled(w, r, v):

    x, y, z = w
    rho, sigma,beta = v
    f = [sigma*(y-x),x*(rho-z)-y,x*y-beta*z ]
    return f




v = [rho,sigma,beta]
w0 =[x0,y0,z0]

wsol = odeint(coupled, w0, t, args=(v,))

with open('cha1', 'w') as f:

    for t1, w1 in zip(t, wsol):
        print >> f, t1, w1[0], w1[1],w1[2]

t, x1, y1, z1 = loadtxt('cha1', unpack=True)

plt.plot(t,x)
plt.plot(t,x1)
plt.show()
plt.plot(t,y)
plt.plot(t,y1)
plt.show()
plt.plot(t,z)
plt.plot(t,z1)
plt.show()

xs=x
ys=y
zs=z

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xs, ys, zs)
xs=x1
ys=y1
zs=z1
#ax.plot(xs, ys, zs)

plt.show()
