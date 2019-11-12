import turtle

bob=turtle.Turtle()

bob.speed(0)
turtle.colormode(255)

def spike(distance):
    for times in range(distance):
        c =times*12
        bob.color(times*2,0,0)
        bob.width(times+10)
        bob.fd(distance)
        bob.left(10)
def spikeflower(distance):
    for times in range(11):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times*35)
def tile( c ):
    polygon(4,200, c )
    for times in range(4):
        polygon(3,50,"black")
        bob.fd(50)
        polygon(3,50,"black")
        bob.fd(50)
        polygon(3,50,"black")
        bob.fd(50)
        polygon(3,50,"black")
        bob.fd(50)
        bob.lt(90)
def rowtile(c):
    for times in range(8):
        tile(c)
        bob.fd(200)

def square(distance):
    for times in range(4):
        bob.fd(distance)
        bob.lt(90)

def triangle(distance):
    for times in range(3):
        bob.fd(distance)
        bob.lt(120)

def polygon(sides,distance,c):
    bob.color( c )
    angle=360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.fd(distance)
        bob.lt(angle)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance,c):
    bob.color( c )
    bob.begin_fill()
    for times in range(5):
        bob.fd(distance)
        bob.lt(144)
    bob.end_fill()

def explosion(distance,c):
    bob.color( c )
    bob.begin_fill()
    for times in range(8):
        bob.fd(ditance)
        bob.lt(135)
    bob.end_fill()

def figure1(distance,size,color):
    bob.color( color )
    bob.begin_fill()
    bob.circle(size)
    bob.fd(distance)
    bob.circle(size)
    bob.left(45)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(45)
    bob.circle(size)
    bob.fd(distance)
    bob.circle(size)
    bob.end_fill()

def monster(color):
    bob.color(color)
    bob.begin_fill()
    bob.lt(90)
    bob.fd(100)
    bob.circle(50)
    bob.lt(90)
    bob.forward(100)
    bob.lt(90)
    bob.fd(100)
    bob.lt(135)
    bob.fd(35)
    bob.rt(90)
    bob.fd(35)
    bob.lt(135)
    bob.fd(35)
    bob.rt(90)
    bob.fd(35)
    bob.end_fill()

def fadingTriangle():
  for times in range(100):
      c =(times * 2,0,times * 2)
      polygon(3,450-times *4, c )
      bob.left(135)
    
