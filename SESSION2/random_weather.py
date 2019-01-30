from random import randint

w = randint(3,7)

if w < 30:
    print("Rainy")
elif w < 60:
    print("Cloud")
else:
    print("Sunny")
    