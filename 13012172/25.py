def f(n):
    list = []
    for i in range(2, n+1):
        if n % i == 0 and i % 2 == 0:
            list.append(i)
    if len(list) == 6:
        print(*list)


for i in range(125256, 125331):
    f(i)