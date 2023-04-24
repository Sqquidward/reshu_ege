import math

file = open('26.txt')
n = int(file.readline())
list_skidka, list_bez = [], []
for i in range(n):
    digit = int(file.readline())
    if digit > 100:
        list_skidka.append(digit)
    else:
        list_bez.append(digit)




list_skidka = sorted(list_skidka)
count = len(list_skidka) // 2

summa =0
max_elem = list_skidka[count-1]
for i in range(count):
    summa += list_skidka[i] / 100 * 70
summa = math.ceil(summa)

for j in range(count, len(list_skidka)):
    summa += list_skidka[j]
for i in range(len(list_bez)):
    summa += list_bez[i]
print(max_elem, summa)

