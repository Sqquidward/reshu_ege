###25
def f(n):
    count, mx = 0, 0
    for i in range(2, (n+1)//2):
        if n % i == 0:
            count += 1
            mx = max(mx, i)

        elif count > 3:
            break
    if count == 3:
        print(n, mx)


for i in range(289123456, 389123457):
    f(i)
#289123468 72280867