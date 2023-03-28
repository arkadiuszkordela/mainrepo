# In this exercise I have to create a smile game with randomly loot from boxes.

import random
from enum import Enum

print("""Welcome in this simple game without
any sense but... I hope that you will have fun.""")

events = Enum('event', ['chest', 'nothing'])

events_dictionary = {
                        events.chest: 0.6,
                        events.nothing: 0.4 
                    }

events_list = list(events_dictionary.keys())
events_probability = list(events_dictionary.values()) 

colors = Enum('colors', ['white', 'black', 'blue'])

colors_dictionary = {
                        colors.white: 0.5,
                        colors.black: 0.4,
                        colors.blue: 0.1
                    }

colors_list = list(colors_dictionary.keys())
colors_probability = list(colors_dictionary.values())

game_length = 5

while game_length > 0:
    player_answer = input('Do you want to move forward? (y/n)')
    if (player_answer == "y"):
        print("Okay, let's go!")
        drawn_event = random.choices(events_list, events_probability)[0]
        if (drawn_event == events.chest):
            print('You found a chest!')
            drawn_color = random.choices(colors_list, colors_probability)[0]
            if (drawn_color == colors.white):
                print('Your chest is white. There is a 100 gold coins inside')
            elif (drawn_color == colors.black):
                print('Your chest is black. There is a 200 gold coins inside')
            elif (drawn_color == colors.blue):
                print('Your chest is blue. There is a 500 gold coins inside')                                                                        
        elif (drawn_event == events.nothing):
            print('You found nothing!')
    else:
        print('Sorry. You lost!')
        continue
    game_length = game_length - 1

    print('Done! I hope that you liked it...')
    