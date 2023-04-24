def f(m, n, A):
    return (((3 * m) + (4 *n)) > 66) or (m <= A) or (n < A)



for A in range(200):
    flag = True
    for m in range(200):
        for n in range(200):
            if not(f(m, n, A)):
                flag = False

    if flag == True:
       print(A)
       break