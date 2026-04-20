import random
dice_art = {
    1: ("""
┌---------┐
|         |
|    ●    |
|         |
└---------┘"""),
    2: ("""
┌---------┐
| ●       |
|         |
|       ● |
└---------┘"""),
    3: ("""
┌---------┐
| ●       |
|    ●    |
|       ● |
└---------┘"""),
    4: ("""
┌---------┐
| ●     ● |
|         |
| ●     ● |
└---------┘"""),
    5: ("""
┌---------┐
| ●     ● |
|    ●    |
| ●     ● |
└---------┘"""),
    6: ("""
┌---------┐
| ●     ● |
| ●     ● |
| ●     ● |
└---------┘""")
}


dice = []
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

for value in dice:
    print(dice_art.get(value))


total = sum(dice)

print(f"total: {total}")