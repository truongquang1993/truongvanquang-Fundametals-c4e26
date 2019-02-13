items = ["Pho", "Bun", "Mien"]

# For i
for i in range(len(items)):
    print(items[i])

# For each
print(" ")

no = 1

for food in items:
    print(no, food, sep=", ")
    no += 1

for i, food in enumerate(items, 1):
    print(i, food, sep= ", ")