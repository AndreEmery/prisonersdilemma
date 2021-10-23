from player import player

class roundrobin(object):
    def __init__(self, players):
        self.players=players
        self.nplayers=len(players)

    def match(self, player1, player2, turn):
        p1=player1.strategy(player2, turn)
        p2=player2.strategy(player1, turn)
        player1.addHistory(p1)
        player2.addHistory(p2)
        return [(3-p1)*p2, (3-p2)*p1]
                
    
    def run(self, turns):
        """Plays a roundrobin style tournament"""

        roundresults = []
        for i in range(len(self.players)):
            filler=[]
            for j in range(len(self.players)):
                filler.append(0)
            roundresults.append(filler)
        for i in range(len(self.players)):
            for j in range(len(self.players)-i):
                if i==j:
                    roundresults[i][i]=0
                    continue
                score=[0,0]
                for k in range(turns):
                    matchresult=self.match(self.players[i],self.players[j+i],k)
                    score[0]+=matchresult[0]
                    score[1]+=matchresult[1]
                roundresults[i][j+i]=score[0]
                roundresults[j+i][i]=score[1]
                self.players[i].clear()
                self.players[j+i].clear()
        self.players[0].addScore(69)
        return roundresults
