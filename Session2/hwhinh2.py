from turtle import *
for i in range (3,7):
    for j in range(i):
        if i % 2 == 0:     # chia phan nguyen cho 2 du 0
            color('red')
        else:
            color('blue')
        forward(100)
        left(360/i)

mainloop()