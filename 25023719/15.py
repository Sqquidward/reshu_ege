for A in range(200):
    flag = True
    for x in range(200):
        for y in range(200):
            if not((x >= 9) or (2 * x < y) or ( x * y < A)):
                flag = False
    if flag == True:
        print(A)