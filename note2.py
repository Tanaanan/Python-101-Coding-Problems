Alabic_input = input('Enter only 5 Arabic number:')
Alabic_num = '0123456789'
Thai_num = '๐๑๒๓๔๕๖๗๘๙'
thai = ''
for m in Alabic_input :
    index = Alabic_num.find(m)
    print(index)
    '''if index != -1 :
        thai = thai + Thai_num[index]
print(' Thai number is' , thai)'''
