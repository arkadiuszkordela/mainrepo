# In this exercise I have to load names and surnames from a file. Next I have to separate names and surnames and save them in different files.

names_and_surnames = []

with open('names_and_surnames.txt', 'r', encoding = 'UTF-8') as file:
          for line in file:
                  names_and_surnames.append(tuple(line.replace('\n', '').split(' ')))

with open('only_names.txt', 'w', encoding = 'UTF-8') as file:
        for line in names_and_surnames:
                file.write(line[0] + '\n')

with open('only_surnames.txt', 'w', encoding = 'UTF-8') as file:
        for line in names_and_surnames:
                if(len(line) == 2):
                        file.write(line[1] + '\n')
                else:
                        file.write('\n')