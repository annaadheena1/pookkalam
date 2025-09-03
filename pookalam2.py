import turtle
screen=turtle.Screen()
screen.title("Turtle graphics example")
pen=turtle.Turtle()
pen.width(4)
pen.speed(0)

turtle.colormode(255)

def circ(r,x1,x2,x3):
    pen.color(x1,x2,x3)
    pen.penup()
    pen.setheading(270)
    pen.fd(r)
    pen.setheading(0)
    pen.pendown()
    pen.begin_fill()
    pen.circle(r)
    pen.end_fill()

    pen.penup()
    pen.setheading(90)
    pen.fd(r)
    pen.setheading(0)
    pen.down()
    
def petal1(length=100):
    pen.color(250, 220, 110)
    pen.begin_fill()
    for i in range(17):
        pen.fd(length)
        pen.circle(length/4,208)
        pen.fd(length)
        pen.rt(180)
        pen.rt(150)
    pen.end_fill()

def petal3(length=100):
    pen.color(237, 179, 92)
    pen.begin_fill()
    for i in range(17):
        pen.fd(length)
        pen.circle(length/4,208)
        pen.fd(length)
        pen.lt(180)
        pen.rt(150)
    pen.end_fill()

def petal2(length=100):
    pen.color(47, 135, 35)
    pen.begin_fill()
    for i in range(70):
        pen.fd(length)
        pen.circle(length/4,208)
        pen.fd(length)
        pen.lt(180)
        pen.lt(-17)
    pen.end_fill()

def petal4(length=100):
    pen.color(234,162,33)
    pen.begin_fill()
    for i in range(17):
        pen.fd(length)
        pen.circle(length/4,208)
        pen.fd(length)
        pen.lt(180)
        pen.rt(150)
    pen.end_fill()

def smallflower():
    pen.color(168, 27, 36)
    pen.begin_fill()
    for i in range (10):
        pen.circle(100,360,6)
        pen.lt(75)
        pen.lt(70)
    pen.end_fill()

def end():
    for i in range(20):
        pen.color('pink')
        pen.fd(i)
        pen.rt(76)

circ(320,13, 43, 9)
petal2(230)
petal1(200)
petal3(200)
petal4(200)
smallflower()
end()



