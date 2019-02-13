items = ["An", "Di choi", "Xem phim"]
idex = ["I", "II", "III", "IV", "V"]

for i in items:
    print(i.upper())

for i, fvr in enumerate(items, 1):
    print(i, fvr.upper(), sep=". ")

for i, fvr in enumerate(items, 0):
    print(idex[i], fvr.upper(), sep=". ")

for i, fvr in zip(idex, items):
    print(i, fvr, sep = ". ")

a = 0
for fvr in items:
    print(idex[a], fvr.upper(), sep=". ", end = " ")
    a += 1