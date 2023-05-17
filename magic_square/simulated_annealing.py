import math
import random

class simulated_annealing:
    def __init__(self, problem, schedule):
        self.problem = problem
        self.schedule = schedule

    def solve(self):
        current = self.problem
        for t in range(1, len(self.schedule)):
            T = self.schedule[t]
            if T == 0:
                return current
            next_state = random.choice(current.successors())
            deltaE = next_state.value() - current.value()
            if deltaE > 0:
                current = next_state
            else:
                if random.random() < math.exp(deltaE / T):
                    current = next_state
        return current

