import random

x = random.randint(1, 100)
user_num = 0
cnt = 0

while True:
    user_num = int(input('Try to guess the number from 1 to 100: '))
    cnt += 1
    if user_num == x:
        print(f'That is correct! You guessed number within {cnt} attempts!')
        if input('Want to play again? "Y/N": ') == 'Y':
            x = random.randint(1, 100)
            cnt = 0
        else:
            print('Thank you, goodbye!')
            break
    elif user_num > x:
        print('The number is lower')
    else:
        print('The number is higher')