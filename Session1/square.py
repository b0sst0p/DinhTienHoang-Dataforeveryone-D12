import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.fillcolor('yellow')
t.begin_fill()
for i in range(4):
    t.forward(50)
    t.right(90)
t.end_fill()
wn.mainloop()
