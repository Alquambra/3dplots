import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import LinearLocator
from matplotlib.animation import FuncAnimation
from matplotlib import cm
from mpl_toolkits import mplot3d


xpointsnumber = 10
ypointsnumber = 10

xnumbers = [i for i in range(1, xpointsnumber + 1)]
ynumbers = [[i] * xpointsnumber for i in range(1, ypointsnumber + 1)]
x = np.array(xnumbers * ypointsnumber).reshape(ypointsnumber, xpointsnumber)
y = np.array(ynumbers)
z = np.random.uniform(7.5, 9.5, xpointsnumber * ypointsnumber).reshape(ypointsnumber, xpointsnumber)


def animate(i):
    global xpointsnumber
    global ypointsnumber
    global x, y, z

    index = 0
    # x = np.insert(x, ypointsnumber, x[0], axis=0)

    # x = np.delete(x, 0, 0)


    print(xpointsnumber, ypointsnumber)
    print()
    print(x)
    print()
    print(y)
    print()
    print(z)
    print()

    ax.plot_surface(x, y, z, cmap=colormap_reversed, linewidth=0, antialiased=False)

    y = np.insert(y, xpointsnumber, ypointsnumber + 1, axis=0)
    z = np.append(z, [np.random.uniform(5.5, 6.5, xpointsnumber)], axis=0)
    y = np.delete(y, 0, 0)
    z = np.delete(z, 0, 0)
    ax.set_xlim3d(0, xpointsnumber + 5)
    ax.set_ylim3d(0, ypointsnumber + 5)
    ax.set_zlim3d(5, 15)
    ypointsnumber = ypointsnumber + 1
    index += 1

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

colormap = cm.get_cmap('Blues')
colormap_reversed = colormap.reversed()

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_xlabel('xlabel, cm')
ax.set_ylabel('ylabel, cm')
ax.set_zlabel('depth, cm')

ax.set_title('bottom model')

ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.tight_layout()
plt.show()

