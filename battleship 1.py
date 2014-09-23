

class Ship():
    size = None



class Carrier(Ship):
    size = 5



class Battleship(Ship):
    size = 4




class Patrolboat(Ship):
    size = 3

class Submarine (Ship):
    size = 3





player_carrier = Carrier()
enemy_carrier = Carrier()

print(player_carrier.size)
print(enemy_carrier.size)
