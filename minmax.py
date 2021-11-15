A = int(input("")) # รับค่า input เป็นตัวกำหนด range
s = [] # create blank string to kept an input.

for i in range(A):
    b = int(input("")) # receive number from input
    s.append(b) # append an input to string

s.sort() # เรียงลำดับจากน้อยไปมาก
print(s[0]) #print 1st index (min)
print(s[-1])#print last index (max)