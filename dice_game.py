import random

def main():
    def roll_dice():
        dice_total = random.randint(1,6) + random.randint(1,6)
        return dice_total
    p1 = input("enter player 1's name:\n")
    p2 = input("enter player 2's name:\n")

    roll1 = roll_dice()
    roll2 = roll_dice()
    print(p1, 'rolled a', roll1)
    print(p2, 'rolled a', roll2)

    if roll1 == roll2:
        print('You tied')
    elif roll1 > roll2:
        print(p1, "won the game")
    else: 
        print(p2, "won the game")
main()