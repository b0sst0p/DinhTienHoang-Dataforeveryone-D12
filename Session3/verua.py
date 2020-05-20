from turtle import *
from random import choice
shape('turtle')
speed('fastest')
a =['red','blue','brown','yellow','grey']
for i in range(3,8):
    for j in range(i):
        forward(50)
        left(360/i)
        if i==3:
            color('red')
        elif i==4:
            color('blue')
        elif i==5:
            color('brown')
        elif i==6:
            color('yellow')
        else:
            color('grey')
mainloop()