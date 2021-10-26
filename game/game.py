from player import player
from roundrobin import roundrobin

#initializing variables
players = []
bestplayers = []
psize=40
gens=80
turnstot=40

#population initial player list
for i in range(psize):
    players.append(player(.4,0,0,0,.4))

#runs 1 initial round
roundrunner=roundrobin(players)
roundresults=roundrunner.run(turnstot)

#sort players by fitness, or their score
players.sort(key=player.getScore, reverse=True)

for obj in players:
    print(obj)
print("-"*50)

bestplayers.append(players[0])

for i in range(gens):
    #culling bottom third
    for j in range(int(psize/3)):
        players.pop(int(psize*2/3)+1)
    #repopulating with top third
    for j in range(int(psize/3)):
        base, alpha, beta, gamma, mutate = players[j].getParameters()
        players.append(player(base,alpha,beta,gamma,mutate))
    #run round
    roundresults=roundrunner.run(turnstot)
    #sort list
    players.sort(key=player.getScore, reverse=True)
    bestplayers.append(players[0])
    for obj in players:
        print(obj)
    print("-"*20)
for player in bestplayers:
    print(player)
