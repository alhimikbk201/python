print('введите координаты первой точки')
x1 = float(input('введите x '))
y1 = float(input('введите y '))
print('введите координаты второй точки')
x2 = float(input('введете x '))
y2 = float(input('введите y '))

r = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
a = round(r, 2)
print(a)

          
