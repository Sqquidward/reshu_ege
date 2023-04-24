list =[[0] * 10000 for j in range(10000)]
print(list)
file = open('26.txt')
n = int(file.readline())
for i in range(n):
    a, b = file.readline().split()
    list[int(a)-1][int(b)-1] = 1


count, mx, ryd = 0, 0, 0
for i in range(10000):
    for j in range(10000):
        if list[i][j] == 0:
            count += 1
            if count > mx:
                mx = count
                ryd = i
        else:
            count = 0
print(mx, ryd)
