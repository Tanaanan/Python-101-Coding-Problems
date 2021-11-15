num = input('Enter value in mm, cm, and m: ')
convert = input('Enter unit to convert in mm, cm, m: ')
if "cm" in  num:
    cal = float(num[0:-2])
    cal = float(cal)
    if "m" == convert : 
        print('Value after unit conversion is ' + str(cal/100) + 'm')
    elif "mm" == convert :
        print('Value after unit conversion is ' + str(cal*10) + 'mm')
elif "mm" in  num:
    cal = float(num[0:-2])
    if "m" == convert :
        print('Value after unit conversion is ' + str(cal/1000) + 'm')
    elif "cm" == convert :
        print('Value after unit conversion is ' + str(cal/10) + 'cm')
else:
    num = str(num.strip('m'))
    num = float(num)
    if "cm" == convert:
        print('Value after unit conversion is ' + str(num*100) + ' m')
    elif "mm" == convert :
        print('Value after unit conversion is ' + str(num*1000) + 'mm')