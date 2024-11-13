#eltrix
for i in range(0x80000000):
    test = 0
    final = 0
    for j in range(32):
        test = i >> j
        final = (test & 1) + 2 * final
        print(test, final)
    if final == i:
        print(i)
        break

