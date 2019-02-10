from random import randint

w = randint(0,100)

while True:
    number = input("Enter a number you chose:")
    if number.isdigit():
        a = int(number)
        if a < w:
            number = input("Your number is lowwer than number random, Enter a number: ")
        elif a > w:
            number = input("Your number is upper than number random, Enter a number: ")
        else a == w:
            print("Congratulation, Your number is number random")
            break
    else:
        print("You must enter a number: ")