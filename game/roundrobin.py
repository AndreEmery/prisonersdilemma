from player import player

class roundrobin(object):
    def __init__(self, players):
        self.players=players
        self.nplayers=len(players)

    def match(self, player1, player2, turn, turnstot):
        p1=player1.strategy(player2, turn, turnstot)
        p2=player2.strategy(player1, turn, turnstot)
        player1.addHistory(p1)
        player2.addHistory(p2)
        return [(4-p1)*p2+1-p1, (4-p2)*p1+1-p2]
                
    
    def run(self, turnstot):
        """Plays a roundrobin style tournament"""

        roundresults = []
        for i in range(len(self.players)):
            filler=[]
            for j in range(len(self.players)):
                filler.append(0)
            roundresults.append(filler)

        for player in self.players:
            player.clearScore()
            
        for i in range(len(self.players)):
            for j in range(len(self.players)-i):
                if j==0:
                    roundresults[i][i]=0
                    continue
                score=[0,0]
                for k in range(turnstot):
                    matchresult=self.match(self.players[i],self.players[j+i],k, turnstot)
                    score[0]+=matchresult[0]
                    score[1]+=matchresult[1]
                roundresults[i][j+i]=score[0]
                self.players[i].addScore(score[0])
                roundresults[j+i][i]=score[1]
                self.players[j+i].addScore(score[1])
                self.players[i].clearHistory()
                self.players[j+i].clearHistory()
        return roundresults
