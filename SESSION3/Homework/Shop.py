items = ["T-Shirt","Sweater"]

while True:
    slt = input("Welcome to our shop, what do you want (C, R, U, D)?")
    if slt == "R" or slt == "r":
        print("Our items:", *items, sep=",")
    elif slt == "C" or slt == "c":
        items.append(input("Enter new item:"))
        print("Our items:", *items, sep=", ")
    elif slt == "U" or slt == "u":
        u_item = int(input("Update position?"))
        items[u_item] = input("New item?")
        print("Our items:", *items, sep=", ")
    elif slt == "D" or slt == "d":
        u_item = int(input("Delete position?"))
        items.remove(items[u_item])
        print("Our items:", *items, sep=", ")
    else:
        print("You have to input C, R, U or D")
