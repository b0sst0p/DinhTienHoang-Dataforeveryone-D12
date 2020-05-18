import turtle
wn = turtle.Screen()
t= turtle.Turtle()
t.fillcolor('yellow')
t.begin_fill()
for i in range(3): 
    t.forward(80) 
    t.left(120) 
t.end_fill()
wn.mainloop()