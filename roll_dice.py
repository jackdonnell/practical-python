import random
roll = random.randint(1,6)
guess = int(input('guess the dice\'s roll:\n'))
if guess == roll:
    print('Correct! they rolled a ' + str(roll))
else: 
    print("nope you were wrong it rolled a " + str(roll))