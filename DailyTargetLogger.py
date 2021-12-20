import datetime

def gettime():
    return datetime.datetime.now()


def log(Target):
    if Target == "Project" or "Certification" or "Aptitude" or "More":
        status = int(input("Enter 1 for Done and 2 for Not-Done"))
        if status == 1:
            value = input("Type here\n")
            with open("Work-done.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif status == 2:
            value = input("Type here\n")
            with open("Work-not-done.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
         
    else:
        print("plz enter valid input Project/certification/Aptitude ")


def retrieve(Target):
    status = int(input("Enter 1 for Done and 2 for Not-Done"))

    if status == 1:
        with open("Work-done.txt") as f:
            for i in f:
                print(i, end="")
    elif status == 2:
        with open("Work-not-done.txt") as f:
            for i in f:
                print(i, end="")
    else:
            print("plz enter valid input (1/2)")
 
while True:
    print("\nDaily Target Achieved: ")
    mode = input("\nDo you want to log or retrieve ?\nEnter l for logging and r for retriving:  ")
    if mode == "l":
        b =input("Choose what you did today ?\n  1.Project\n  2.Certification\n  3.Aptitude\n  4.More\n  Your answer:")
        log(b)
    elif mode == "r":
        b =print(("Which file you want to see?\n  1.Work-done\n  2.Work-not-done "))
        retrieve(b)
    else:
        print("plz enter valid mode (l/r)")    

# In this project, I used time module, Functions of python, 
# writing/appending and reading file and alot of COMMON SENSE.