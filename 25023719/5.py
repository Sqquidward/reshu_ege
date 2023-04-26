def f(n):
    n_2 = bin(n)[2:]
    if n % 3 == 0:
        return int(n_2 + n_2[-3:], 2)
    else:
        return int(n_2 + bin((n%3) * 3)[2:], 2)



for i in range(100):
    if f(i) >76:
        print(i)
        break