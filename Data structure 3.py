import string
l = []
while True:
    a = input('Enter string: ')
    if 'end' in a:
        break
    l.append(a)
    l.sort
set_l = set(l)
list_l = list(set_l)
print(list_l)
print('''******************************
*     Alphabet Counting      *
******************************''')
A_Z_letter = string.ascii_letters
text = ''
for m in range (A_Z_letter):