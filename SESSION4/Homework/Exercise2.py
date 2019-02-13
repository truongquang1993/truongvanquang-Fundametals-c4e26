inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
for i in inventory.keys():
    print(i, ":", inventory[i])
print("\n")

# 1
inventory.get("pocket")

for i in inventory.keys():
    print(i, ":", inventory[i])
print("\n")

# 2
inventory["pocket"] = ["seashell", "strange berry", "lint"]

for i in inventory.keys():
    print(i, ":", inventory[i])
print("\n")

# 3
inventory["backpack"].remove("dagger")

for i in inventory.keys():
    print(i, ":", inventory[i])
print("\n")

# 4
inventory["gold"] += 50

for i in inventory.keys():
    print(i, ":", inventory[i])
print("\n")