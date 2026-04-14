from random import randint

count = 0

def rollDice():
    user = input("Roll the dice? (y/n): ")
    cmnd = user[0].lower()
    if cmnd == 'y':
        print(f"({randint(1, 7)}, {randint(1, 7)})")
        global count
        count += 1
        rollDice()
    elif cmnd == 'n':
        print("Dice Rolling End")
        print(f"Dice Rolled: {count} times")
        return
    else:
        print("Invalid Input")
        rollDice()
    
rollDice()



