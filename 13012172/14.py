def f(i, n):
    b = ''
    while i > 0:
        b += str(i%n)
        i//=n
    return b[::-1]

primer = 2*(216**6) + 3*(36**9) - 432

print(f(primer, 6).count('5'))