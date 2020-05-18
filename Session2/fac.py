a=input('enter number whose factorial is required')
b= int(a)
factorial=1
i=1
while i<=b:
    factorial = factorial*i
    i=i+1
print('factorial of',b,'is',str(factorial))
