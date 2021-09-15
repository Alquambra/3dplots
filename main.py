import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import LinearLocator
from matplotlib.animation import FuncAnimation
from matplotlib import cm
from mpl_toolkits import mplot3d




# def draw_bottom(xpointsnumber, ypointsnumber):
#     fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
#
#     xnumbers = [i for i in range(1, xpointsnumber + 1)]
#     ynumbers = [[i] * xpointsnumber for i in range(1, ypointsnumber + 1)]
#     x = np.array(xnumbers * ypointsnumber).reshape(ypointsnumber, xpointsnumber)
#     y = np.array(ynumbers)
#     z = np.random.uniform(7.5, 9.5, xpointsnumber * ypointsnumber).reshape(ypointsnumber, xpointsnumber)
#     # x = np.insert(x, ypointsnumber, x[0], axis=0)
#     # y = np.insert(y, ypointsnumber, ypointsnumber + 1, axis=0)
#     # z = np.append(z, [np.random.uniform(5.5, 6.5, xpointsnumber)], axis=0)
#
#     y = np.delete(y, 0, 0)
#
#     # X, Y, Z = x, y, z
#
#     print(x)
#     print()
#     print(y)
#     print()
#     print(z)
#
#     # ax.set_xlim3d(0, xpointsnumber)
#     # ax.set_ylim3d(0, ypointsnumber)
#     # ax.set_zlim3d(5, 15)
#     #
#     # colormap = cm.get_cmap('Blues')
#     # colormap_reversed = colormap.reversed()
#     #
#     # surf = ax.plot_surface(X, Y, Z, cmap=colormap_reversed, linewidth=0, antialiased=False)
#     # ax.zaxis.set_major_locator(LinearLocator(10))
#     # ax.zaxis.set_major_formatter('{x:.02f}')
#     # fig.colorbar(surf, shrink=0.5, aspect=5)
#     # ax.set_xlabel('xlabel, cm')
#     # ax.set_ylabel('ylabel, cm')
#     # ax.set_zlabel('depth, cm')
#     #
#     # ax.set_title('bottom model')
#     #
#     # plt.show()
#
#
#
#
#
#
# draw_bottom(5, 10)


y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(y)
y = np.delete(y, 0, 0)
print(y)
