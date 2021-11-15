print('''Select 2 options
 - 1 encrypt with ROT 13
 - 2 decrypt with ROT 13''')
print("")
chose = int(input('Choose option: '))
charc = input('Enter text: ')
UpperWord = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
LowerWord = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
rot_13 = ""
if chose == 1 and chose != 2:    
    for c in charc :
        if c in UpperWord :
            rot_13 = rot_13 + UpperWord[UpperWord.find(c)+13]
        elif c in LowerWord :
            rot_13 = rot_13 + LowerWord[LowerWord.find(c)+13]
        else:
            rot_13=rot_13+c
    print('Ciphertext is','"'+rot_13+'"')

if chose == 2 and chose != 1:    
    for c in charc :
        if c in UpperWord :
            rot_13 = rot_13 + UpperWord[UpperWord.find(c)-13]
        elif c in LowerWord :
            rot_13 = rot_13 + LowerWord[LowerWord.find(c)-13]
        else:
            rot_13=rot_13+c
    print('Plaintext is','"'+rot_13+'"')