def f(a, n):
    if a >= 43 and n == 3:
        return True
    elif a >= 43 and n < 3:
        return False
    elif a < 43 and n >= 3:
        return False
    else:
        if n % 2 == 1:
            return f(a + 1, n + 1) and f(a + 4, n + 1) and f(a * 3, n + 1)
        else:
            return f(a+1, n+1) or f(a+4, n+1) or f(a*3, n+1)

for i in range(1, 43):
    if f(i, 0):
        print(i)

