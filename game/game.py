from player import player
from roundrobin import roundrobin

players = []

for i in range(30):
    players.append(player(.25,.25,0,-.1,.1))

roundrunner=roundrobin(players)
turns=15

roundresults=roundrunner.run(15)

print(roundresults)

playerfitness=[]

print(players[0].getScore())
for player in players:
    print(player)