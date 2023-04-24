def f(n):
    for i in range(2, (n+1)//2):
        if n % i == 0:
            return False
    return True
count = 0
for i in range(245690, 245757):
    count += 1
    if f(i):
        print(count, i)