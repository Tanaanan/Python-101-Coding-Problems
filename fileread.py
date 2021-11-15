f = open('filetest.txt', 'w')

for i in range(0,11):
    print("Type number {} in hiragana".format(i))
    number = input("")
    f.write(str(i) + '==' + str(number) + '\n')

print('Writing to file complete')

f.close()