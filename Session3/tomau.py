import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.fillcolor()
t.begin_fill()
for j in range(5):
    for i in range(2):
        t.forward(50*i)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(50*2*i)   
t.end_fill()
wn.mainloop()
