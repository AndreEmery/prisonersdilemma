class roundrobin(object):
    def __init__(self, players):
        self.players=players
        self.nplayers=len(players)

    def match(player1, player2, turn):
        p1=player1.strategy(player2, turn):
        p2=player2.strategy(player1, turn);
        player1.addHistory(p1)
        player2.addHistory(p2)
        return [(3-p1)*p2, (3-p2)*p1]
                
    
    def run(self, turns):
        """Plays a roundrobin style tournament"""

        roundresults = [[0] * nplayers] * nplayers
        for i in len(self.players):
            for j in len(self.players)-i:
                if i==j:
                    roundresults[i][i]=0
                    continue
                score=[0,0]
                for i in turns:
                    matchresult=self.match(players[i],players[j+i])
                    score[1]+=matchresult[1]
                    score[2]+=matchresult[2]
                roundresults[i][j+i]=score[1]
                roundresults[j+i][i]=score[2]
                players[i].clear()
                players[j+i].clear()
        return roundresults
