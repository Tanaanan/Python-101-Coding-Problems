import string
a = input('Enter 5 characters: ')
b = string.ascii_letters
c = (string.ascii_letters[::-1])
d = ''
for m in a :
    index = b.find(m)
    if index != -1 :
        d = d + c[index]
print('Encryption is' , d.lower())