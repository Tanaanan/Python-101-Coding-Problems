l =[]
counter = 1
while counter > 0:
    counter = int(input('Enter number: '))
    l.append(counter)
l.sort()
print('Minimum number is {}' .format(l[1]))
print('Maximum number is {}' .format(l[-1]))
