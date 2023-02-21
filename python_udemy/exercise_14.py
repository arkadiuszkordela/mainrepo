# In this exercise I have to create five rockets whose will move up randomly with random speed.

from random import randint

class Rocket:
    
    def __init__(self):
        self.altitude = 0
        
        random_speed = randint(1, 7)
        self.speed = random_speed
        
    def move_up(self):
        self.altitude += self.speed

    def __str__(self):
        return 'The rocket is on altitude: ' + str(rocket.altitude)

rockets = [Rocket() for _ in range(5)]

for _ in range(10):
    rocket_to_move = randint(0, 4)
    rockets[rocket_to_move].move_up()

for rocket in rockets:
    print(rocket)