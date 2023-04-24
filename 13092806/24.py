###24
strok = open('24-6.txt').read()
strok = strok.replace('ad', 'a d')
strok = strok.replace('da', 'd a')

count, mx = 0, 0
for elem in strok:
    if elem == ' ':
        count = 0
    else:
        count += 1
        if count > mx:
            mx = count
print(mx)