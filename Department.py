p, f, s = 0, 0, 0
for i in range(1, 8):
    for j in range(i + 1, 8):
        for l in range(j + 1, 8):
            if i + j + l == 12:
                if i % 2 == 0:
                    p, f, s = i, j, l
                elif j % 2 == 0:
                    p, f, s = j, i, l
                else:
                    p, f, s = l, i, j
                print(f"{p}, {f}, {s}")
