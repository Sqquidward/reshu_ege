str = open('zadanie24_1.txt').read()
count, mx = 0, 0
for elem in str:
    if elem == 'A':
        count += 1
        if count > mx:
            mx = count
    else:
        count = 0
print(mx)