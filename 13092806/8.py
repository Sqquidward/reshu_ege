from itertools import product
count = 0
for i in product('ЛНОС', repeat = 5):
    count += 1
    print(count, *i)

