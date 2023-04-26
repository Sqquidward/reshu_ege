from itertools import product

st = open('24.txt').read()
for i in product('XYZ', repeat = 2):
    st = st.replace(''.join(i), i[0] + " " + i[1])

count, mx = 0, 0
for elem in st:
    if elem == ' ':
        count = 0
    else:
        count += 1
        if count > mx:
            mx = count
print(mx)