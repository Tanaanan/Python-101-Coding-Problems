import string
stringput = (input("Enter 5 characters: "))
AtoZ = string.ascii_lowercase
reverseAtoZ = (string.ascii_lowercase[::-1])
Total = ''
for m in stringput :
    index = AtoZ.find(m)
    if index != -1 :
        Total = Total + reverseAtoZ[index]


AtoZ_upper = string.ascii_uppercase
reverseAtoZ_upper = (string.ascii_uppercase[::-1])
Total_upper = ''
for y in stringput :
    index = AtoZ_upper.find(y)
    if index != -1 :
        Total = Total + reverseAtoZ_upper[index]
Total = str.lower(Total)
print ("Encryption is " , Total)