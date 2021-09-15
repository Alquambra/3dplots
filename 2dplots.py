import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm

lines = []
y = np.linspace(1, 20, 20)
z = np.random.uniform(10, 20, 20)
cmap = plt.get_cmap('jet', 10)

fig, ax = plt.subplots(1, 1, figsize=(12, 6))

line, = ax.plot(y, z)
line1, = ax.plot(y, np.zeros(20))

ax.set_title('Модель подводного дна в двух измерениях')
ax.set_xlabel('ширина')
ax.set_ylabel('глубина')

ax.set_ylim((0, 30))
ax.grid(True)


def animate(i):
    line1.set_ydata(line._y)
    line.set_ydata(np.random.uniform(10, 20, 20))
    return line


ani = animation.FuncAnimation(fig, animate, interval=1000)

# print(line.__dir__())
# print(line._axes)
# print(line._x)
# print(line._y)
# print(line._xy)
# print(line.axes)
# print(line.get_data)
# print(line.get_xdata)
# print(line.get_ydata)
plt.show()


