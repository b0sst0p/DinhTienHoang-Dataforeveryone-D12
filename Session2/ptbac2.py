a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
delta = b**2 - 4 * a * c
if delta < 0:
    print('vo nghiem')
elif delta==0:
    x= -b/2*a
    print('nghiem kep')
    print('x=',x)
else:
    x1= (-b +delta**(1/2)) / 2*a
    x2 = (-b - delta **(1/2)/2*a)
    print('x1=',x1)
    print('x2=', x2)