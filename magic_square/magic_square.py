import math
import random

class magic_square:
    def __init__(self, n):
        self.n = n
        self.state = [i for i in range(1, n*n+1)]
        random.shuffle(self.state)

    def value(self):
        target_sum = self.n * (self.n * self.n + 1) // 2
        row_sum = [sum(self.state[i*self.n:(i+1)*self.n]) for i in range(self.n)]
        col_sum = [sum(self.state[i::self.n]) for i in range(self.n)]
        diag_sum = [sum(self.state[::self.n+1]), sum(self.state[self.n-1:self.n**2-1:self.n-1])]
        return -sum(abs(target_sum - x) for x in row_sum + col_sum + diag_sum)

    def successors(self):
        successors = []
        for i in range(self.n * self.n):
            for j in range(i+1, self.n * self.n):
                new_state = self.state[:]
                new_state[i], new_state[j] = new_state[j], new_state[i]
                successors.append(magic_square(self.n))
                successors[-1].state = new_state
        return successors