from random import *
from calc import evaluate
def generate_quiz():
    x = randint(1,9)
    y = randint(1,9)
    op = choice(["+", "-", "*", "/"])
    z = randint(-1,1)
    result = evaluate(x, y, op) + z
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    
    if user_choice == True:
        if evaluate(x, y, op) == result:
            return True
        else:
            return False
    elif user_choice == False:
        if evaluate(x, y, op) == result:
            return False
        else:
            return True
    pass
