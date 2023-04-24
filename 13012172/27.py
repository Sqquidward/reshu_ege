file = open('27-A.txt')

n = int(file.readline())
list = []
for i in range(n):
    list.append(int(file.readline()))



for i in range(len(list)):
    sum = 0
    for j in range(len(list), 0, -1):
        sum += list[j]
