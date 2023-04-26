file = open('26.txt')
k = int(file.readline())
n = int(file.readline())
list = []
for i in range(n):
    list.append(file.readline().split())
list_a = []
for i in range(k):
    list_a.append([0, 0])
count = 0
posledhya = 0
for i in range(n):
    for j in range(k):
        if int(list[i][0]) > int(list_a[j][1]) + 1:
            list_a[j] = list[i]
            posledhya = j
            count += 1
print(count, posledhya)


