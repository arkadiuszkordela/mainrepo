# It is a exercise where I have to point the lists with a least one even number.

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

numbers_1 = [number % 2 == 0
for number in number_list_1]
numbers_2 = [number % 2 == 0
for number in number_list_2]

print(any(numbers_1))
print(any(numbers_2))
### Method 2. /\

def eve_nr(list):
    return any([number % 2 == 0 for number in list])

print(eve_nr(number_list_1))
print(eve_nr(number_list_2))
### Method 3. /\

# In this exercise I have to point who from that two persons below can Python and JavaScript.

john = {
    'name': 'John Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'C++']
}

jane = {
    'name': 'Jane Smith',
    'age': 25,
    'skills': ['Python', 'Java']
}

def skills(list):
    for value in list:
        if value == "Python":
            print("Python ok!")
        elif value == "JavaScript":
            print("JavaScript ok!")
        elif value != "Python":
            print("No matter skill.")
        elif value != "JavaScript":
            print("No matter skill.")
