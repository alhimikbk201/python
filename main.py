a = int(input('введите четверть плоскости координат '))

if (a == 1):
    print('x > 0, y > 0')
elif (a == 2):
    print('x < 0, y > 0')
elif (a == 3):
    print('x < 0, y < 0')
elif(a == 4):
    print('x > 0 and y < 0')
else:
    print('ошибка ввода данных')            
