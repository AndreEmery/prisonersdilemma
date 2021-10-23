import random

class player(object):
    """Player class for the tournament"""

    def __init__(self, base, alpha, beta, gamma, mutate):
        """creates player object
        base, alpha, beta, gamma are all coefficients in determining % chance of cooperating with opponent, depending on the game state
        mutate factor adds variability to coefficients"""
        self.history=[]
        self.base=base * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)
        self.alpha=alpha * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)
        self.beta=beta * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)
        self.gamma=gamma * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)
        self.mutate=mutate * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)

    def strategy(player, turn):
        try:
            opp1=player.getLast()
        except IndexError:
            opp1=.5
        try:
            opp2=player.get2ndLast()
        except IndexError:
            opp2=.5
        coop=base + alpha*opp1 + beta*opp2 + gamma*turn
        if random.uniform(0,1)<coop:
            return 1
        return 0

    def getLast(self):
        try:
            return self.history[-1]
        except IndexError:
            return IndexError

    def get2ndLast(self):
        try:
            return self.history[-2]
        except IndexError:
            return IndexError

    def addHistory(value):
        self.history.append(value)

    def clear(self):
        self.history=[]
