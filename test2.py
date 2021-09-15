import matplotlib.colors
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
from pprint import pprint


# Настройка стиля графиков
plt.style.use('seaborn')

lines = []
x = np.linspace(11, 20, 10)
zeros = np.zeros(10)


# настройка цветовой гаммы
cmap = cm.get_cmap('seismic', 10)
colors = cmap(np.linspace(0, 1, 10))[::-1]
norm = matplotlib.colors.Normalize()
sm = plt.cm.ScalarMappable(cmap=cm.get_cmap('seismic'), norm=norm)

# создание полотна для рисования графиков
fig, ax = plt.subplots(figsize=(12, 6))

for i in range(10):
    # line, = ax.plot(x, zeros, lw=1, color=colors[i])
    lines.append(ax)

for index, ax in enumerate(lines):
    ax.plot(x, zeros)


ax.set_title('Модель подводного дна в двух измерениях')
ax.set_xlabel('Ширина')
ax.set_ylabel('Глубина')

ax.set_ylim((0, 40))
ax.grid(True)


# функция для рисования графика в реальном времени
def animate(i):
    y = np.random.uniform(10, 20, 10)
    lines[0].set_ydata(y)
    lines[0].set_zorder(10)
    for index, ax in enumerate(lines[1:]):
        y = lines[index]._y
        ax.set_ydata(y)
        ax.set_zorder(9 - index)
        # ax.fill_between(x, y, where=y<=0, color=colors[''])


ani = animation.FuncAnimation(fig, animate, interval=1000)


# настройка цветовой шкалы для графика
cbar = fig.colorbar(sm, ticks=[0, 1])
cbar.ax.set_yticklabels(['Дальше', 'Ближе'])


# рисование итогового графика
plt.show()