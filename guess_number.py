import random

r = random.randint(1, 100)
while True:
    num = input('Guess a number: ')
    num = int(num)
    if num == r:
        print('Bingo!!!')
        break
    elif num > r:
        print('Your answer is bigger.')
    elif num < r:
        print('Your answer is smaller')