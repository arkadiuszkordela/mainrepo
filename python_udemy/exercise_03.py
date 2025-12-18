# In this exercise I have to generate six random number (without repeating) from some set of numbers.

print(' ')
print('********** M1')
print(' ')

import random

all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
amount = [1, 2, 3, 4, 5, 6]

drawn_number = random.sample(all_numbers, len(amount))

print(' ')
print('Drawn numbers are:')
print(drawn_number)
print(' ')

# Now I will try to make a more functional program like this.

print(' ')
print('********** M2')
print(' ')

list_1 = int(input('How many numbers should be in a set for drawn: '))
list_2 = int(input('How many numbers do you want to draw: '))

all_numbers_list = [i + 1 for i in range(list_1)]
amount_list = [0] * list_2

drawn_number_2 = random.sample(all_numbers_list, len(amount_list))

print(' ')
print('Drawn numbers are:')
print(drawn_number_2)
print(' ')