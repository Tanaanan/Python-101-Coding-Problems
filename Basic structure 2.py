import string
l = []
counter = 0
m = 1
for m in range (m,m+1):
    while counter > -1:
        counter = int(input('Enter number #{}: ' .format(m)))
        m = m + 1
        if m > 20:
            break
        l.append(counter)
l.sort()
l = set(l)
l = str(l)
l = l.strip('{ }')
l = l.replace(',','')
print('Unique numbers is', l)
l = list(l)
l = l.replace('','')
print(l[::2])