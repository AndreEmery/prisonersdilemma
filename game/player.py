import random

class player(object):
    """Player class for the tournament"""

    def __init__(self, base, alpha, beta, gamma, mutate):
        """creates player object
        base, alpha, beta, gamma are all coefficients in determining % chance of cooperating with opponent, depending on the game state
        mutate factor adds variability to coefficients"""
        self.score=0
        self.history=[]
        self.base=max(-1,min(1,base * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)))
        self.alpha=max(-1,min(1,alpha * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)))
        self.beta=max(-1,min(1,beta * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)))
        self.gamma=gamma * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)
        self.mutate=max(-1,min(1,mutate * random.uniform(1-mutate,1+mutate) + .1*random.uniform(-mutate,mutate)))

    def strategy(self, player, turn, turnstot):
        opp1=player.getLastIndex(1)
        if opp1==IndexError:
            opp1=.3
            
        opp2=player.getLastIndex(2)
        if opp2==IndexError:
            opp2=.3

        coop=self.base + self.alpha*opp1 + 0*self.beta*opp2 + self.gamma*turn*turn/turnstot/turnstot
        if random.uniform(0,1)<coop:
            return 1
        return 0

    def getLastIndex(self,index):
        try:
            return self.history[-index]
        except IndexError:
            return IndexError

    #def get2ndLast(self):
      #  try:
     #       return self.history[-2]
    #    except IndexError:
   #         return IndexError

    def addHistory(self,value):
        self.history.append(value)

    def addScore(self,value):
        self.score=self.score+value

    def getParameters(self):
        return [self.base, self.alpha, self.beta, self.gamma, self.mutate]

    def getScore(self):
        return self.score

    def __str__(self):
        string=""
        for element in self.getParameters():
            string+='{number:.{digits}f}'.format(number=element,digits=4)+"\t"
        return string
    #str(self.base)+", "+str(self.alpha)+", "+str(self.beta)+", "+str(self.gamma)+", "+str(self.mutate)

    def clearHistory(self):
        self.history=[]

    def clearScore(self):
        self.score=0
