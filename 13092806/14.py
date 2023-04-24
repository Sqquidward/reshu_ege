def f(i, n):
    b = ''
    while i >0:
        b += str(i% n)
        i//=n
    return b[::-1]
answer = (81 ** 15) + (3 ** 22) - 27
print(f(answer, 9), f(answer, 9).count('8'))