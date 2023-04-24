str = 68 * '8'

while '222' in str or '888' in str:
    if '222' in str:
        str = str.replace('222', '8', 1)
    else:
        str = str.replace('888', '2', 1)
print(str)

