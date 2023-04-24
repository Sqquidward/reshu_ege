from itertools import product
count = 0
for i in product('КОР', repeat = 5):
    count +=1
    print(count, *i)

