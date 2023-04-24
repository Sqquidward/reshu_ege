def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return n // 2
    elif n % 2 == 1:
        return 1 + f(n - 1)

for i in range(1000):
    if f(i) == 12:
        print(i)
        break

