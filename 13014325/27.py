file = open('B.txt')
n = int(file.readline())
list = []
for i in range(n):
    list.append(int(file.readline()))
mx = 0
count = 0
for i in range(0, len(list)-1):
    for j in range(i+1, len(list)):
        if int(list[i]) > int(list[j]) and (list[i] + list[j]) % 120 == 0:
            count = list[i] + list[j]
            if count > mx:
                mx = count
                answer = ''
                answer+= str(list[i]) +  ' ' + str(list[j])
if answer == '':
    print('00')
else:
    print(answer)

