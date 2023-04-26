def f(x, y, z, w):
    return not(y and not(x)) and not(x == z) and w

print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w):
                    print(x, y, z, w, f(x, y, z, w))
yxzw