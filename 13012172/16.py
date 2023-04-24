def F(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    elif n > 3:
        return  F(n-3) + F(n-2)

print(F(12))
