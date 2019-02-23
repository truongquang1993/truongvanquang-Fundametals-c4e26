def get_even_list(l):
    so_chan = []
    for i in l:
        if i % 2 == 0:
            so_chan.append(i)
    print(*so_chan, sep=", ")
l = [1, 1, 3, 5, 6, 8, 7]

get_even_list(l)