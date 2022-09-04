import os
import random
min = 1
max = 10
count = 0
price = 0
choice = 'y'
os.system("cls")
run = int(input('How Many Times You Wan to play? : '))
if run == 1:
    while choice == 'y':
        count += 1
        os.system("cls")
        rnum = random.randint(min, max)
        # print(rnum)
        unum = int(input('Enter Your guess: '))

        if rnum == unum:
            print("You Won!!")
            price += 10
        else:
            print('You Lose')
            print('The Right number is ', rnum)
        choice = input('Want to play again?(y/n) ')
    if choice == 'n':
        print('')
        print('You Won $', price)
        print('Thanks For Playing! Your total cost is: $', count)
elif run == 0:
    print('please enter a positive integer greater than 0')
else:
    for i in range(0, run):
        count += 1
        rnum = random.randint(min, max)
        # print(rnum)
        print('')
        print('Game #', i+1)
        # unum=random.randint(min,max)
        unum = int(input('Enter Your guess: '))
        # print("your AUto guess: ",unum)

        if rnum == unum:
            print("You Won!!\nYou Guessed it right!")
            print("**********************")
            price += 10
        else:
            print('\aYou Lose')
            print('The Right number is ', rnum)
            print("__________________________")
    print('You Won $', price)
    print('Thanks For Playing! Your total cost is: $', count)
