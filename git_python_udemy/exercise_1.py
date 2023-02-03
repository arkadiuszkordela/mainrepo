# It is a exercise where I have to point the lists with a least one even number.

print(' ')
print('********** M1')
print(' ')

number_list_1 = [3, 5, 10, 13, 17]
number_list_2 = [3, 7, 13, 15, 23]

def even_number(list):
    for number in list:
        if number % 2 == 0:
            return True
    
    return False

print(even_number(number_list_1))
print(even_number(number_list_2))
### Method 1. /\

print(' ')
print('********** M2')
print(' ')

numbers_1 = [number % 2 == 0
for number in number_list_1]
numbers_2 = [number % 2 == 0
for number in number_list_2]

print(any(numbers_1))
print(any(numbers_2))
### Method 2. /\

print(' ')
print('********** M3')
print(' ')

def eve_nr(list):
    return any([number % 2 == 0 for number in list])

print(eve_nr(number_list_1))
print(eve_nr(number_list_2))
### Method 3. /\