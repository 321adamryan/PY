
import random

suspects = ['green','white','scarlet','plum','mustard','peacock']
weapons = ['knife','pipe','rope','candlestick','gun','wrench']
rooms = ['conservatory','billiard','library','study','hall','lounge','dining','kitchen','ballroom']

def solution():

    return [suspects[random.randint(0,5)], weapons[random.randint(0,5)], rooms[random.randint(0,8)]]

print(solution())
