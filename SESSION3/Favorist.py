items = ["An", "Di choi", "Xem phim"]

while True:
    new_item = input("So thich moi: ")

    items.append(new_item)

    print(*items, sep=", ")


