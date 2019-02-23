def is_inside(pos_check, region):
    if pos_check[0] < region[0] or pos_check[0] > region[0] + region[2]:
        s = False
    else:
        if pos_check[1] < region[1] or pos_check[1] > region[1] + region[3]:
            s = False
        else:
            s = True
    print(s)

is_inside([200, 120],[140, 60, 100, 200])