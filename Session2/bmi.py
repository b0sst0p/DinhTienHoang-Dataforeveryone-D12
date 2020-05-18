a = int(input('height ='))
b=a/100
c = int (input('weight ='))
bmi = c/(a*a)
if bmi <16:
    print('severely underweight')
elif bmi>16 and bmi<18.5:
    print('underweight')
elif bmi>18.5 and bmi<25:
    print('normal')
elif bmi>25 and bmi<30:
    print('overweight')
elif bmi >30:
    print('obese')
else:
    print('unknown')