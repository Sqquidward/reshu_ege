file = open('17-9.txt')
list = [int(x) for x in file]

sm, count = 0, 0

for i in range(len(list)-1):
    for j in range(i+1, len(list)):
        if (list[i] + list[j]) % 2 != 0 and (list[i] * list[j]) % 3 == 0:
            count += 1
            sm = max(sm, list[i] + list[j])
print(count, sm)