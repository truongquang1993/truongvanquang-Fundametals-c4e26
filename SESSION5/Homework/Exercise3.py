print("Answer the following algebra question:\nIf x = 8, then what is the value of 4(x+3) ?")
print("1. 35\n2. 36\n3. 40\n4. 44")

b = 0

ex1 = input("Your choie:")
while not ex1.isdigit():
    ex1 = input("You must input a digit. Your choie:")

if int(ex1) == 4:
    print("Bingo")
    b +=1
else:
    print(":(")

print("Estimate this answer (exact caculation not needed):\nJack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?")
print("1. About 55\n2. About 65\n3. About 75\n4. About 85")

ex2 = input("Your choie:")
while not ex2.isdigit():
    ex2 = input("You must input a digit. Your choie:")

if int(ex2) == 2:
    print("Bingo")
    b +=1
else:
    print(":(")

print("You correctly answer", b, "out of 2 questions")