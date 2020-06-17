import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1  # count = count + 1
    num = input('Guess a number: ')
    num = int(num)
    if num == r:
        print('Bingo!!!')
        print(count, 'times') #第一個方式 (老師)
        break
    elif num > r:
        print('Your answer is bigger.')
    elif num < r:
        print('Your answer is smaller')
    print(count, 'times')
#print(count, 'times') #第二個方式 (自己)

   