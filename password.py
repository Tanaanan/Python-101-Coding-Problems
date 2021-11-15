import time
start = time.time()
input1 = input("")
input2 = input("")
input3 = input("")
password = input("")

input_list = [input1, input2, input3]
list_pass = password.split(",")

lenght = []
for i in range(len(list_pass)): # 1 == lenght on 6-12, 0 == lenght not in 6-12
    if len(list_pass[i]) >= 6 and len(list_pass[i]) <= 12:
        lenght.append("1")
    else:
        lenght.append("0")

space = [] # 0 == have space, 1 == don't have space
for i in range(len(list_pass)):
    if " " in list_pass[i]:
        space.append("0")
    else:
        space.append("1")

special_char = [] # 1 == have @,#,$ , 0 == don't have
for i in range (len(list_pass)):
    if "#" in list_pass[i]:
        special_char.append("1")
    elif "$" in list_pass[i]:
        special_char.append("1")
    elif "@" in list_pass[i]:
        special_char.append("1")
    else:
        special_char.append("0")


pass1 = list_pass[0]
s_pass1 = str(pass1)
pass2 = list_pass[1]
s_pass2 = str(pass2)
pass3 = list_pass[2]
s_pass3 = str(pass3)

lower = []
sum_lower = []
digit = []
sum_digit = []
upper = []
sum_upper = []

def lower_alpha (distance):
    for i in range(len(distance)):
        if distance[i].islower() == True:
            lower.append("1")
        else:
            lower.append("0")

def digit_alpha (distance):
    for i in range(len(distance)):
        if distance[i].isdigit() == True:
            digit.append("1")
        else:
            digit.append("0")

def upper_alpha (distance):
    for i in range(len(distance)):
        if distance[i].isupper() == True:
            upper.append("1")
        else:
            upper.append("0")

def sum(len_l,ls):
    if "1" in len_l:
        ls.append("1")
    else:
        ls.append("0")

lower_alpha(s_pass1)  #lower
sum(lower,sum_lower)
lower_alpha(s_pass2)
sum(lower,sum_lower)
lower_alpha(s_pass3)
sum(lower,sum_lower)

digit_alpha(s_pass1) #digit
sum(digit,sum_digit)
digit_alpha(s_pass2)
sum(digit,sum_digit)
digit_alpha(s_pass3)
sum(digit,sum_digit)

upper_alpha(s_pass1) #upper
sum(upper,sum_upper)
upper_alpha(s_pass2)
sum(upper,sum_upper)
upper_alpha(s_pass3)
sum(upper,sum_upper)

check = []
for i in range(len(list_pass)):
    if "111111" in lenght[i]+space[i]+special_char[i]+sum_upper[i]+sum_digit[i]+sum_lower[i]  :
        check.append(True)
    else:
        check.append(False)


print("time =", (time.time()-start)*1000)

#print(check)

for i in range(len(list_pass)):
    if check[i] == bool(1):
        print(list_pass[i] + " (" + input_list[i] + ")")

#print("lenght = ",lenght)
#print("space = ",space)
#print("special_char = ",special_char)
#print('lower = ',sum_lower)
#print("digit = ",sum_digit)
#print("upper = ",sum_upper)

"""test input

Gotan
Tawan
Program
ABd1234@1,a F1#2w3E,2We3345

"""