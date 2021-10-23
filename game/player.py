import random

class player(object):
    """Player class for the tournament"""

    def __init__(self, base, alpha, beta, gamma, mutate):
        """creates player object
        base, alpha, beta, gamma are all coefficients in determining % chance of cooperating with opponent, depending on the game state
        mutate factor adds variability to coefficients"""
        self.score=0
        self.history=[]
        self.base=base * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)
        self.alpha=alpha * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)
        self.beta=beta * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)
        self.gamma=gamma * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)
        self.mutate=mutate * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)

    def strategy(self, player, turn):
        opp1=player.getLast()
        if opp1==IndexError:
            opp1=.5
            
        opp2=player.get2ndLast()
        if opp2==IndexError:
            opp2=.5

        coop=self.base + self.alpha*opp1 + self.beta*opp2 + self.gamma*turn
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

    def addHistory(self,value):
        self.history.append(value)

    def addScore(self,value):
        self.score+=value

    def getScore(self):
        return self.score

    def __str__(self):
        return str(self.base)+", "+str(self.alpha)+", "+str(self.beta)+", "+str(self.gamma)+", "+str(self.mutate)

    def clearHistory(self):
        self.history=[]

    def clearScore(self):
        self.score=0
