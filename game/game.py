from player import player
from roundrobin import roundrobin

players = []
psize=40
gens=120
turnstot=5

for i in range(psize):
    players.append(player(.5,0,0,0,.4))

roundrunner=roundrobin(players)

roundresults=roundrunner.run(turnstot)

#print(roundresults)

players.sort(key=player.getScore, reverse=True)

for i in range(gens):
    for j in range(int(psize/2)):
        players.pop(int(psize/2))
    for j in range(int(psize/2)):
        base, alpha, beta, gamma, mutate = players[j].getParameters()
        players.append(player(beta,alpha,beta,gamma,mutate))
    roundresults=roundrunner.run(turnstot)
    #print(roundresults)
    players.sort(key=player.getScore, reverse=True)

for player in players:
    print(player.getScore(),player)
