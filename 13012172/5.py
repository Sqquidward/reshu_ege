def f(n):
    n = str(n)
    return str(sorted([int(int(n[0]) + int(n[1])), int(int(n[1]) + int(n[2]))])[0]) + str(sorted([int(int(n[0]) + int(n[1])), int(int(n[1]) + int(n[2]))])[1])

for i in range(100, 1000):
    if f(i) == '714':
        print(i)