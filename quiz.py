print("welcome to the simple COMPUTER quiz")

playing = input("Do you want to play ? ")

if playing != "yes":
    quit()

print("Let's play :)")
player_name = input("Enter your name :" )

Score = 0
answer= input("What does OS stands for ?")
if answer.lower()  == "Operating System " :
    print("Correct!")
    Score+=1
else:
    print("InCorrect!")

answer = input("What does DBMS stands for ?")
if answer.lower()  == "Database Mnagement System " :
    print("Correct!")
    Score+=1

else:
    print("InCorrect!")

answer = input("What does CPU stands for ?")
if answer.lower()  == "Central Processing Unit" :
    print("Correct!")
    Score+=1

else:
    print("InCorrect!")

answer = input("What does GPU stands for ?")
if answer.lower()  == "Graphics Processing Unit" :
    print("Correct!")
    Score+=1

else:
    print("InCorrect!")


answer = input("What does RAM stands for ?")
if answer == "Random Access Memory" :
    print("Correct!")
    Score+=1

else:
    print("InCorrect!")


print("You got "+ str(Score)+ " questions correct!")


""" In this project, I used if-else control statements of python and COMMON SENSE. """