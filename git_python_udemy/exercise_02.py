# In this exercise I have to point who from that two persons below can Python and JavaScript.

print(' ')
print('********** M1')
print(' ')

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
        if value == 'Python':
            print('Python ok!')
        elif value == 'JavaScript':
            print('JavaScript ok!')
        elif value != 'Python':
            print('No matter skill.')
        elif value != 'JavaScript':
            print('No matter skill.')
        elif value == 'C++':
            print('No matter skill.')

print('John:')
print(skills(john['skills']))

print(' ')

print('Jane:')
print(skills(jane['skills']))
### Method 1. /\

print(' ')
print('********** M2')
print(' ')
        
def check_skills(person, skills):
    return all(skill in person['skills'] for skill in skills)

required_skills = ['Python', 'JavaScript']

print('John:')
print(check_skills(john, required_skills))

print(' ')

print('Jane:')
print(check_skills(jane, required_skills))
### Method 2. /\