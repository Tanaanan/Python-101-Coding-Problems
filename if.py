import random
print('{:*^30s}'.format('Random Disk'))
number = random.randint(1, 5)
print('อาหารแนะนำวันนี้', end=' ')
if number == 1:
 print('ข้าวราดคะน้าหมูทอด')
elif number == 2:
 print('กระเพราไก่ไข่ดาว')
elif number == 3:
 print('พิซซ่า')
elif number == 4:
 print('ข้าวเหนียวไก่ทอด')
else:
 print('ก๋วยเตี๋ยวต้มยำา')
print('*'*30)