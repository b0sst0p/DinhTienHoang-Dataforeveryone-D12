import turtle
wn = turtle.Screen()
t= turtle.Turtle()
t.begin_fill()
for i in range(6): 
    t.circle(200) 
    t.right(-120) 
    t.circle(200)
    t.right(-150)
t.end_fill()
wn.mainloop()