import turtle
wn = turtle.Screen()
t= turtle.Turtle()
t.speed('fastest')
t.fillcolor('green')
t.begin_fill()
for i in range(360//7): 
    t.circle(50) 
    t.right(-5) 
    
t.end_fill()
wn.mainloop()

