
while True:
    yob_string = input("year of birth: ")
    if yob_string.isdigit():
        yob = int(yob_string)
        if 1920 < yob < 2019:
            break
        else:
        print("You must enter a number, with a number upper 1920 and lowwer 2019")
    else:
        print("You must enter a number: ")
    else int(yob_string) < 1920:
        print("You must enter a number, with a number upper 1920")
    
age = 2019 - yob
print("age:", age)
