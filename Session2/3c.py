#3ci
import pprint
n = 9
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
pprint.pprint(m)


#3cii
import pprint
n = int(input('Enter a number:'))
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
pprint.pprint(m)
#or
n=int(input('Enter a number: '))
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row*col, end="")
    print()