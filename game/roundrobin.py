from player import player

class roundrobin(object):
    def __init__(self, players):
        ###Creates class that can run a round robin style competition on a list of players
        self.players=players
        self.nplayers=len(players)

    def match(self, player1, player2, turn, turnstot):
        #each player calculates their .strategy() using the game's state variables
        p1=player1.strategy(player2, turn, turnstot)
        p2=player2.strategy(player1, turn, turnstot)
        #each player adds their played strategy to their history
        player1.addHistory(p1)
        player2.addHistory(p2)
        #returns the expected value [a,b] for player a and player b
        return [(4-p1)*p2+1-p1, (4-p2)*p1+1-p2]
                
    
    def run(self, turnstot):
        """Runs the roundrobin style tournament"""

        #initializing an n x n matrix for each players total gains vs n other players
        roundresults = []
        for i in range(len(self.players)):
            filler=[]
            for j in range(len(self.players)):
                filler.append(0)
            roundresults.append(filler)

        #making sure score are reset so the natural selection only cares about this round
        for player in self.players:
            player.clearScore()

        #iterating over i and j in matrix
        for i in range(len(self.players)):
            for j in range(len(self.players)-i):
                if j==0:
                    #cannot have player play against himself
                    roundresults[i][i]=0
                    continue
                score=[0,0]

                #each pair of players plays the dilemma game turnstot # of times in a row
                for k in range(turnstot):
                    matchresult=self.match(self.players[i],self.players[j+i],k, turnstot)
                    score[0]+=matchresult[0]
                    score[1]+=matchresult[1]

                #recording scores to both roundresults and player.score
                roundresults[i][j+i]=score[0]
                self.players[i].addScore(score[0])
                roundresults[j+i][i]=score[1]
                self.players[j+i].addScore(score[1])

                #reset pairing history for next pairing
                self.players[i].clearHistory()
                self.players[j+i].clearHistory()
        return roundresults
