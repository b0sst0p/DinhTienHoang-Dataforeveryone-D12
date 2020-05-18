from turtle import *
from random import choice
shape('turtle')
speed('fastest')
a =['blue','red','blue','red']
for i in range(3,7):
    for j in range(i):
        forward(50)
        left(360/i)
        color(choice(a))
mainloop()
