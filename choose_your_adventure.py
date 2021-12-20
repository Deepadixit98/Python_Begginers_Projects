player_name = input("Enter your name: ")
print("Welcome", player_name, "to this adventure!")

print("You are on a dirt road, it has come to an end and you can go left or right. ")

answer = input("Which way would you like to go? (left/right)").lower()

if answer == "left":
    print("You come to a river, you can walk around it or swim accross? ")
    answer = input("Type walk to walk around and swim to swim accross: (swim/walk)")

    if answer == "swim":
        print("You swam acrross and were eaten by an alligator .")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a bridge, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger.Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and they give you gold. You Win!")
        elif answer == "no":
            print("You ignore the stranger and he/she killed you and You Lose!.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for playing", player_name)

""" In this project, I used nested if-else and if-elif control statements 
of python to make a short story of adventure and some COMMON SENSE. """