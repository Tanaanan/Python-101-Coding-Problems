Gender = str(input('Enter Gender (M/W): '))
if Gender == 'M' or Gender == 'W':
    Current_year = int(input('Enter current year: '))
    Birth_year = int(input('Enter your birth year: '))
    Weight = float(input('Enter your weight (kg): '))
    Height = float(input('Enter your height (cm): '))
    Height_m =  float(Height/100)
    Year = (Current_year-Birth_year)
    BMI = float('{:.3f}' .format(Weight/Height_m**2))
    print('- - - - - -')
    print('Your age =', Year)
    print('Your BMI =', BMI)
    if 'M' in Gender:
        BMR = (66.5+(13.75*Weight)+(5.003*Height)-(6.755*Year))
        print('Your BMR = {:.3f}' .format(BMR))
    elif 'W' in Gender:
        BMR = (655.1+(9.563*Weight)+(1.850*Height)-(4.676*Year))
        print('Your BMR = {:.3f}' .format(BMR))
else:
    print('{} is not M or W' .format(Gender))
