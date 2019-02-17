print("Answer the following algebra question:\nIf x = 8, then what is the value of 4(x+3) ?")
print("1. 35\n2. 36\n3. 40\n4. 44")

a = input("Your choie:")
while not a.isdigit():
    a = input("You must input a digit. Your choie:")

if int(a) == 4:
    print("Bingo")
else:
    print(":(")