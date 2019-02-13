items = ["Pho", "Bun", "Mien"]



for i, fvr in enumerate(items, 1):
    print(i, fvr, sep = ". ")

slt = input("What you want to delete?")

while 1 > slt or slt > len(items):

    # 1 > slt or slt > len(items)
    print("You only input number in list, from 1 to", len(items))
    slt = int(input("Inpunt your number:"))

if slt.isdigit():


items.pop(slt)

for i, fvr in enumerate(items, 1):
    print(i, fvr, sep = ". ")

# Chua hoan thien