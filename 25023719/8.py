from itertools import product
count = 0
for i in product('АКЛМНЯ', repeat = 5):
    count += 1
    print(count, ''.join(i))