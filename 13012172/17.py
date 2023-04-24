file = open('17.txt')
list = [int(x) for x in file]

mx, count = 0, 0

for i in range(0, len(list)-1):
    for j in range(i+1, len(list)):
        if (list[i] % 50 == 0 or list[j] % 50 == 0) and (list[i] + list[j]) % 80 == 0:
            count += 1
            mx = max(mx, list[i] + list[j])
print(count, mx)