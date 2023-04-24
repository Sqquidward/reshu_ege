####26
file = open('26.txt')
max, n = file.readline().split()
list = []
for i in range(int(n)):
    list.append(int(file.readline()))
list = sorted(list)
imax = int(max)
count = 0
for i in list:
    count += 1
    imax -= i
    if imax < 0:
        count -= 1
        break

s = 0
for i in range(count-1):
    s += list[i]

for i in range(int(n)-1, -1, -1):
     if list[i] + s <= int(max):
         s = list[i] + s
         print(count, list[i])


