import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation


NUM_ROWS = 20
NUM_COLS = 20
MIDDLE = (NUM_ROWS // 2, NUM_COLS // 2)


class State:
    def __init__(self, block_length=3):
        self.state = np.zeros((NUM_ROWS, NUM_COLS))
        self.block_length = block_length

    def initial_state(self):
        x_mid, y_mid = MIDDLE
        self.state[MIDDLE] = 1
        half_length = self.block_length // 2

        for i in range(1, half_length + 1):
            self.state[x_mid, y_mid - i] = 1
            self.state[x_mid, y_mid + i] = 1

        if self.block_length % 2 == 0:
            self.state[x_mid, y_mid - half_length] = 0

    def next_state(self):
        next_state = np.copy(self.state)
        for x in range(NUM_ROWS):
            for y in range(NUM_COLS):
                if not self.survive((x, y)):
                    next_state[x, y] = 0
                if self.born((x, y)):
                    next_state[x, y] = 1
        self.state = next_state
    
    def survive(self, pos):
        if self.state[pos] == 0:
            return False
        if self.count_neighbor(pos) == 2 or self.count_neighbor(pos) == 3:
            return True
        return False

    def born(self, pos):
        if self.state[pos] == 1:
            return False
        if self.count_neighbor(pos) == 3:
            return True
        return False

    def count_neighbor(self, current_pos):
        count = 0
        x, y = current_pos
        neighbors = []
        if x - 1 >= 0:
            neighbors.append((x - 1, y))
            if y - 1 >= 0:
                neighbors.append((x - 1, y - 1))
            if y + 1 < NUM_COLS:
                neighbors.append((x - 1, y + 1))
        
        if x + 1 < NUM_ROWS:
            neighbors.append((x + 1, y))
            if y - 1 >= 0:
                neighbors.append((x + 1, y - 1))
            if y + 1 < NUM_COLS:
                neighbors.append((x + 1, y + 1))

        if y - 1 >= 0:
            neighbors.append((x, y - 1))
        
        if y + 1 < NUM_COLS:
            neighbors.append((x, y + 1))

        for pos in neighbors:
            if self.state[pos] == 1:
                count += 1

        return count


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

generation = State(8)
generation.initial_state()


def animate(i):
    global generation
    ax1.clear()
    ax1.imshow(generation.state, cmap = mpl.cm.binary)
    generation.next_state()
    

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
