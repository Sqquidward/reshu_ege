for i in range(10):
    for j in range(10):
        for k in range(10000):
            if int(f'11{i}{j}4{k}56') % 211 == 0 and int(f'11{i}{j}4{k}56') < 10 **8:
                print(int(f'11{i}{j}4{k}56'), int(f'11{i}{j}4{k}56')/211)

for i in range(10):
    for j in range(10):
        if int(f'11{i}{j}456') % 211 == 0 and int(f'11{i}{j}456') < 10 **8:
                print(int(f'11{i}{j}456'), int(f'11{i}{j}456')/211)
