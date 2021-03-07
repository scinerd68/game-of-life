import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation


NUM_ROWS = 8
NUM_COLS = 8


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

data = np.zeros((NUM_ROWS, NUM_COLS))
pos = (0, 0)
data[pos] = 1


def move_tile(data, pos):
    x, y = pos
    if x == len(data) - 1 and y == len(data) - 1:
        x = 0
        y = 0
    elif y + 1 >= len(data):
        x += 1
        y = 0
    else:
        y += 1
    
    new_pos = (x, y)
    data[new_pos] = 1
    data[pos] = 0
    return data, new_pos


def animate(i):
    global data
    global pos 
    ax1.clear()
    ax1.imshow(data, cmap = mpl.cm.binary)
    data, pos = move_tile(data, pos)


ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()


# for i in range(10):
#     print(data)
#     data, pos = move_tile(data, pos)
#     print()