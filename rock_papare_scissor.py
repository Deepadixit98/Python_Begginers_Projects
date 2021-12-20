import random

user_wins = 0
computer_wins = 0

Options = ["rock", "paper","scissors"]
while True:
    user_input = input("Choose Rock / Paper/ Scissors or Q to quit. ").lower()
    if user_input == "q":
        break

    if user_input not in Options  :
        continue

    random_number = random.randint(0, 2)
    # rock=0, paper = 1, Scissors= 2 i.e, indices of the list options

    computer_chose = Options[random_number]
    print("Computer chose", computer_chose + ".")

    if user_input == "rock" and computer_chose == "scissors":
        print("YOU WON !")
        user_wins +=1
        
    elif user_input == "paper" and computer_chose == "rock":
        print("YOU WON !")
        user_wins +=1
   
    elif user_input == "scissors" and computer_chose == "paper":
        print("YOU WON !")
        user_wins +=1

    else :
        print("YOU LOST !")
        computer_wins +=1

print("You won", user_wins, "times.") 

print("computer won", computer_wins, "times.") 

print("GoodBye!")


""" In this project, I used random module, if and elif control
statements and while (infinite) loop of python and some COMMON SENSE. """