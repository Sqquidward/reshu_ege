def f(n):
    n_2 = bin(n)[2:]
    return int(n_2[::-1], 2)

for i in range(100):
    if f(i) == 13:
        print(i)
        break

