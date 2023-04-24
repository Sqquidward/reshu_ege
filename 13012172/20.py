def f(a, b, n):
    if a+b >= 41 and n == 3:
        return True
    elif a+b >= 41 and n < 3:
        return False
    elif a+b < 41 and n == 3:
        return False
    else:
        if n % 2 == 1:
            return f(a + 1, b + 2, n + 1) and f(a + 2, b + 1, n + 1) and f(a * 2, b, n + 1) and f(a, b * 2, n + 1)
        else:
            return f(a+1, b+2, n+1) or f(a+2, b+1, n+1) or f(a*2, b, n+1) or f(a, b*2, n+1)

for i in range(1, 33):
    if f(8, i, 0):
        print(i)