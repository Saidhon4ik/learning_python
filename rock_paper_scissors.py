import random

options = ("rock","paper","scissors")

computer = random.choice(options)
running = True


while running:
    player = None
    while player not in options:
        player = input("Enter a choice(rock, paper, scissors): ")

    print(f"Computer picks {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")

    else:
        print("you lose")


    if not input("Play again?(y/n)").lower() == "y":
        running = False

print("thanks for plauing, have a great day")