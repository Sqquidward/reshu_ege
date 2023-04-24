def f(x, y, z, w):
    return (x <= (y == w)) and (y == (w <= z))
print('x y z w f')
st = ''
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w):
                    print(x, y, z, w, f(x, y, z, w))
                st = str(x) + str(y) + str(w) + str(z)
                if not(f(x, y, z, w)) and st.count('0') == 3:
                    print(x, y, z, w, f(x, y, z, w))

#yxwz