

def f(n):
    sm = 0
    for i in n:
        sm += int(i)
    return sm

for i in range(4, 100):
    st = '3'+ ('5' * i)
    while '25' in st or '355' in st or '555' in st:
        if '25' in st:
            st = st.replace('25', '32', 1)
        elif '355' in st:
            st = st.replace('355', '25', 1)
        elif '555' in st:
            st = st.replace('555', '3', 1)
    if f(st) == 17:
        print(i)
        break
