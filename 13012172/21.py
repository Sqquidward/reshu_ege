def f(a, b, n):
    if a+b >= 41 and (n == 2 or n == 4):
        return True
    elif a+b >= 41 and n < 4:
        return False
    elif a+b < 41 and n == 4:
        return False
    else:
        if n % 2 == 0:
            return f(a + 1, b + 2, n + 1) and f(a + 2, b + 1, n + 1) and f(a * 2, b, n + 1) and f(a, b * 2, n + 1)
        else:
            return f(a+1, b+2, n+1) or f(a+2, b+1, n+1) or f(a*2, b, n+1) or f(a, b*2, n+1)

def f1(a, b, n):
    if a+b >= 41 and n == 2:
        return True
    elif a+b >= 41 and n < 2:
        return False
    elif a+b < 41 and n == 2:
        return False
    else:
        if n % 2 == 0:
            return f1(a + 1, b + 2, n + 1) and f1(a + 2, b + 1, n + 1) and f1(a * 2, b, n + 1) and f1(a, b * 2, n + 1)
        else:
            return f1(a+1, b+2, n+1) or f1(a+2, b+1, n+1) or f1(a*2, b, n+1) or f1(a, b*2, n+1)

for i in range(1, 33):
    if f(8, i, 0) and not(f1(8, i, 0)):
        print(i)