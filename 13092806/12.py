def f(n):
    sm = 0
    n = n.replace('>', '')
    for i in n:
        sm += int(i)

    for i in range(2, (sm+1)//2):
        if sm % i == 0:
            return False
    return True

mn = 100
for i in range(1, 100):
    st = '>' + ('0' * 39) + ('1' * i) + ('2' * 39)

    while '>1' in st or '>2' in st or '>0' in st:
        if '>1' in st:
            st = st.replace('>1', '22>', 1)
        if '>2' in st:
            st = st.replace('>2', '2>', 1)
        if '>0' in st:
            st = st.replace('>0', '1>', 1)
    if f(st):
        mn = min(mn, i)
print(mn)
