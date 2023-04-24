#####27
file = open('27_B.txt')
n = int(file.readline())
list = []
for i in range(n):
    list.append(int(file.readline()))

count, mx, para = 0, 0, ''
for i in range(n-1):
    for j in range(i+1, n):
        if (list[i] % 160 != list[j] % 160) and (list[i] % 7 == 0 or list[j] % 7 == 0):
            count = list[i] + list[j]
            if count > mx:
                mx = count
                para = f'{list[i]} {list[j]}'
if para == '':
    print('00')
else:
    print(para)

