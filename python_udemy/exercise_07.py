# In this exercise I have to create program which will open and print a file whose name will be given by a user.

while True:
    opened_file = input('Enter the name of the file to open. (With extension!)')
    try:
        with open(opened_file, "r", encoding='UTF-8') as file:
            for line in file:
                print(line)
            break
    except:
        print('That file does not exist. Please try again.')