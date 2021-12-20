import random

top_of_range = input("Enter the top of range : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)

no_of_guesses = 0

while True:
    no_of_guesses += 1
    user_guess = input("What's you'r guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were ABOVE the number!")
    else:
        print("You were BELLOW the number!")
    
print("You got it in", no_of_guesses, "guesses")

""" In this project, I used random module, if-else control
statements and while (infinite) loop of python and COMMON SENSE. """