a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

D = b*b - 4*a*c

if a == 0:
    otv = 'Так низя'
else:
    if D < 0:
        otv = 'Уравнение имеет только мнимые корни'
    elif D == 0:
        x = -b / 2*a
        otv = 'x = %6.2f' % x
    elif D > 0:
        x1 = (-b + D**0.5)/2*a
        x2 = (-b - D**0.5)/2*a
        otv = 'x1 = %6.2f, x2= %6.2f' % (x1, x2)

print(otv)
1
