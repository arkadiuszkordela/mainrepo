# In this exercise I have to load names and surnames from a file. Nest I have to separate names and surnames and save them in different files.

with open('names.txt', 'r', encoding = 'UTF-8') as file:
          for line in file:
                  print(line)