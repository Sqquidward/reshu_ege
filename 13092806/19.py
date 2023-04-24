def f(x, n):
    if x >= 34 and n == 2:
        return True
    elif n >= 34 and n < 2:
        return False
    elif n < 34 and n >= 2:
        return False
    else:
        if n % 2 == 0:
            return f(x + 1, n + 1) and f(x + 2, n + 1) and f(x * 2, n + 1)

        else:
            return f(x+1, n+1) or f(x+2, n+1) or f(x*2, n+1)

for i in range(1, 34):
    if f(i, 0):
        print(i)
        break
