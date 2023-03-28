# I have to create a program which will show me how many word "Arkadiusz" are in file I will load.

def count_word(file_path, word):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return words.count(word)

file_path = 'names_and_surnames.txt'
word = 'Arkadiusz'
word_count = count_word(file_path, word)

print(f'Number of "{word}" in the file: {word_count}')