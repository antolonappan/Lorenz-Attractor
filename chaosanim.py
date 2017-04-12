import numpy as np
from scipy import integrate

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation


def coupled((x, y, z), t0, sigma=10., beta=8./3, rho=28.0):
   return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]



x0 = [[1,1,1]]


t = np.linspace(1e-5, 100, 10000)
x_t = np.asarray([integrate.odeint(coupled, x0i, t)
                  for x0i in x0])


fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], projection='3d')
ax.axis('off')


colors = plt.cm.jet(np.linspace(0, 1, 1))


lines = sum([ax.plot([], [], [], '-', c=c)
           for c in colors], [])
pts = sum([ax.plot([], [], [], 'o', c=c)
           for c in colors], [])

ax.set_xlim((-25, 25))
ax.set_ylim((-35, 35))
ax.set_zlim((5, 55))


ax.view_init(30, 0)


def init():
    for line, pt in zip(lines, pts):
        line.set_data([], [])
        line.set_3d_properties([])

        pt.set_data([], [])
        pt.set_3d_properties([])
    return lines + pts

def animate(i):
   
    i = (8 * i) % x_t.shape[1]

    for line, pt, xi in zip(lines, pts, x_t):
        x, y, z = xi[:i].T
        line.set_data(x, y)
        line.set_3d_properties(z)

        pt.set_data(x[-1:], y[-1:])
        pt.set_3d_properties(z[-1:])

    ax.view_init(0, 0.05 * i)
    fig.canvas.draw()
    return lines + pts


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=3000, interval=.1, blit=True)

plt.show()
