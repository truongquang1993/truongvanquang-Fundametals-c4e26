n = int(input("Enter a number :  "))
if n%2:
    for i in range(1, n, 2):
        print("x", end="*")
    print("x")
else:    
    for i in range(1, n, 2):
        print("x", end="*")