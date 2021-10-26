from player import player
from roundrobin import roundrobin

#initializing variables
players = []
psize=40
gens=120
turnstot=5

#population initial player list
for i in range(psize):
    players.append(player(.5,0,0,0,.4))

#runs 1 initial round
roundrunner=roundrobin(players)
roundresults=roundrunner.run(turnstot)

#sort players by fitness, or their score
players.sort(key=player.getScore, reverse=True)

for i in range(gens):
    #culling bottom third
    for j in range(int(psize/3)):
        players.pop(int(psize/3))
    #repopulating with top third
    for j in range(int(psize/3)):
        base, alpha, beta, gamma, mutate = players[j].getParameters()
        players.append(player(beta,alpha,beta,gamma,mutate))
    #run round
    roundresults=roundrunner.run(turnstot)
    #sort list
    players.sort(key=player.getScore, reverse=True)

for player in players:
    print(player.getScore(),player)
