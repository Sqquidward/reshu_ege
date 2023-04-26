file = open('17.txt')
list = [int(x) for x in file]

mx = 0
for i in range(len(list)):
        if len(str(list[i])) == 2:
            mx = max(mx, list[i])

count, mxx = 0, 0
for i in range(len(list)-1):
    if ((len(str(list[i])) == 2 and len(str(list[i+1])) != 2) or (len(str(list[i])) != 2 and len(str(list[i+1])) == 2)) and (list[i] + list[i+1]) % mx == 0:
        print(list[i], list[i + 1])
        count += 1
        mxx = max(mxx, list[i] + list[i+1])
print(count, mxx)