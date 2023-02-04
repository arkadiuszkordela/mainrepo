# In this exercise I have to generate six random number (without repeating) from some set of numbers.

import random

all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
amount = [1, 2, 3, 4, 5, 6]

drawn_number1 = random.sample(all_numbers, len(amount))

print('Drawn numbers are:')
print(drawn_number1)