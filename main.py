xyz = ["X", "Y", "Z"]
a = []

for i in range(3):
   
    a.append(int(input(f"введите значения предикат {xyz[i]}")))

left = not (a[0] or a[1] or a[2])

right = not a[0] and not a[1] and not a[2]

resolt = left == right

if(resolt == True):
    print('утверждение истино')
else:
    print('утверждене ложно')    





          
