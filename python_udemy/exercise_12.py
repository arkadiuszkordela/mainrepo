# I have to create a program that will infinitely generate numbers multiplied by themselves using the yield function.

x = int(input('How many numbers do you want to multiply?'))

def squared_numbers(n):
    for i in range(n):
        yield i * i

gen = squared_numbers(x)
for num in gen:
    print(num)