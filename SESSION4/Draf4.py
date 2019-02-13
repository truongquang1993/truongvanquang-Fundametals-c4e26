items = ["Pho", "Bun", "Mien"]


print("Hi, these are my favorist:")

for i, fvr in enumerate(items, 1):
    print(i, fvr, sep = ". ")

slt = int(input("Position you want to delete?"))

while 1 > slt or slt > len(items):

    # 1 > slt or slt > len(items)
    print("You only input number in list, from 1 to", len(items))
    slt = int(input("Inpunt your number:"))



items.pop(slt)

for i, fvr in enumerate(items, 1):
    print(i, fvr, sep = ". ")