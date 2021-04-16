import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class State:
    def __init__(self, block_size=(5, 5), random=True):
        self.state = np.zeros(block_size)
        self.block_size = block_size
        self.random = random

    def initial_state(self):
        if self.random:
            proba_0 = 0.5
            initial_block = np.random.choice([0, 1], size=self.block_size, p=[proba_0, 1-proba_0])
        else:
            initial_block=np.ones(self.block_size)
        self.state = np.pad(initial_block, pad_width=(self.block_size, self.block_size), mode='constant', constant_values=0)

    def next_state(self):
        next_state = np.copy(self.state)
        for x in range(self.state.shape[0]):
            for y in range(self.state.shape[1]):
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
            if y + 1 < self.state.shape[1]:
                neighbors.append((x - 1, y + 1))
        
        if x + 1 < self.state.shape[0]:
            neighbors.append((x + 1, y))
            if y - 1 >= 0:
                neighbors.append((x + 1, y - 1))
            if y + 1 < self.state.shape[1]:
                neighbors.append((x + 1, y + 1))

        if y - 1 >= 0:
            neighbors.append((x, y - 1))
        
        if y + 1 < self.state.shape[1]:
            neighbors.append((x, y + 1))

        for pos in neighbors:
            if self.state[pos] == 1:
                count += 1

        return count


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

generation = State()
generation.initial_state()


def animate(i):
    global generation
    ax1.clear()
    ax1.imshow(generation.state, cmap = mpl.cm.binary)
    generation.next_state()
    

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
