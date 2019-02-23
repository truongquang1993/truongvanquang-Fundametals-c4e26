from random import randint, choice
# import calc
from calc import evaluate
bre = True
while bre:
    x = randint(1,9)
    y = randint(1,9)
    pt = choice(["+", "-", "*", "/"])
    z = randint(-1,1)
    r = evaluate(x, y, pt) + z

    # string formatting
    s = f"{x} {pt} {y} = {r}"
    print(s)
    
# Muốn tìm thư viện ở đâu VD: random._file_
    # user_answer = input("y/n? (exit())")
    # if user_answer == "exit()":
    #     bre = False
    # elif r == x pt y and user_answer == "y":
    #     print("Yay\n")
    # elif r== x + y and user_answer =="n":
    #     print("nang\n")
    # elif r != x + y and user_answer =="y":
    #     print("nang\n")
    # elif r != x + y and user_answer =="n":
    #     print("Yay\n")
    # else:
    #     print("nang\n")
    
