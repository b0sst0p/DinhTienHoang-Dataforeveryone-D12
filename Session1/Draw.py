
import turtle
wn = turtle.Screen()
wn = wn.bgcolor("red")
st = turtle.Turtle()
st.shape("turtle")
st.pensize(5)
st.speed(10)
st2 = turtle.Turtle()
st2.color("green")
st2.pensize(5)
st2.shape("square")
st2.speed(10)
st3 = turtle.Turtle()
st3.color("green")
st3.pensize(5)
st3.speed(10)
def stshape():
    st.forward(20)
    st.right(120)
    st.forward(20)
    st.right(120)
    st.forward(20)
    st.right(120)
def st2shape():
    st2.forward(20)
    st2.right(90)
    st2.forward(20)
    st2.right(90)
    st2.forward(20)
    st2.right(90)
    st2.forward(20)
    st2.right(90)
def st3shape():
    st3.forward(20)
    st3.right(72)
    st3.forward(20)
    st3.right(72)
    st3.forward(20)
    st3.right(72)
    st3.forward(20)
    st3.right(72)
    st3.forward(20)
    st3.right(72)
    st3.forward(20)
    st3.right(72)
def circleloop():
    x1 = 0
    y1 = 0
    x2 = 50
    y2 = 50
    x3 = 100
    y3 = 100
    for i in range(20):
        for x in ("blue", "purple", "orange", "green"):
            st.up()
            st.goto(x1 + 100, y1 + 100)
            x1 = x1 + 10
            y1 = y1 + 10
            st.down()
            st.begin_fill()
            stshape()
            st.end_fill()
            st.stamp()
            st.color(x)
            st2.up()
            st2.goto(x2 + 100, y2 + 100)
            x2 = x2 + 10
            y2 = y2 + 10
            st2.down()
            st2.begin_fill()
            st2shape()
            st2.end_fill()
            st2.stamp()
            st2.color(x)
            st3.up()
            st3.goto(x3 + 100, y3 + 100)
            x3 = x3 + 10
            y3 = y3 + 10
            st3.down()
            st3.begin_fill()
            st3shape()
            st3.end_fill()
            st3.color(x)
        st.stamp()
        st2.stamp()
        st3.stamp()
        print(i + 1)
circleloop()