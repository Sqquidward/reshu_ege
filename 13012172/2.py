def f(x, y, z, w):
    return (not(z) == y) <= ((w and not(x)) == (y and x))
print('x y z w f')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not(f(x, y, z, w)):
                    print(x, y, z, w, int(f(x, y, z, w)))

#zwxy