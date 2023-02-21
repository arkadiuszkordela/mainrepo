# In this exercise I have to make a two lists with five cards from a set.

import random

card_list = ["9(a)", "9(b)", "9(c)", "9(d)",
            "10(a)", "10(b)", "10(c)", "10(d)",
            "Jack(a)", "Jack(b)", "Jack(c)", "Jack(d)",
            "Queen(a)", "Queen(b)", "Queen(c)", "Queen(d)",
            "King(a)", "King(b)", "King(c)", "King(d)",
            "Ace(a)", "Ace(b)", "Ace(c)", "Ace(d)",
            "Joker(a)", "Joker(b)"]

shuffle_cards = random.shuffle(card_list)

player_one = []
player_two = []

for x in random.sample(range(5), 5):
    player_one.append(card_list.pop(x))

for x in random.sample(range(5), 5):
    player_two.append(card_list.pop(x))

print(' ')
print('Player one cards:')
print(player_one)

print(' ')
print('Player two cards:')
print(player_two)