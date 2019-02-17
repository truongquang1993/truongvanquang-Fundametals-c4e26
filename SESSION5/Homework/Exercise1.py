prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

p_list = [prices, stock]

for k in p_list[0].keys():
    print(k)
    print("price:", p_list[0][k], "\nstock:", p_list[1][k], "\n")

total = 0

for k in p_list[0].keys():
    total += p_list[0][k]*p_list[1][k]

print("Total:", total)