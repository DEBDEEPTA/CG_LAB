
# 1. FUNCTION TO DRAW A RECTANGLEd
# 2. FUNCTION TO DRAW A CIRCLE
# 3. FUNCTIONS TO PERFORM OPERATIONS ON 2D OBJECTS
        # 3.1 FUNCTION TO "TRANSLATE" A 2D OBJECT
        # 3.2 FUNCTION TO "ROTATE" A 2D OBJECT
        # 3.2 FUNCTION TO "SCALE" A 2D OBJECT

import turtle

scr = turtle.Screen()          # SETTING TURTLE SCREEN
scr.bgcolor("white")

t = turtle.Turtle()            # CREATING TURTLE INSTANCE
t.speed(0)                     # SETTING DRAWING SPEED
t.pensize(2)                   # SETTING PEN SIZE

def rectangle(x,y,w,h,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    for var in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def circle(x,y,r,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.circle(r)

def translate(x,y,dx,dy):
    t.penup()
    t.goto((x+dx),(y+dy))
    t.pendown()

def rotate(x,y,angle):
    t.penup()
    t.goto(x,y)
    t.setheading(angle)
    t.pendown()

def scale(x,y,sx,sy):
    t.penup()
    t.goto(x*sx,y*sy)
    t.pendown()

#DRAWING USING THE FUNCTIONS
rectangle(-200, 0, 100, 50, "blue")
translate(-200, 0, 200, 0)
rectangle(0, 0, 100, 50, "blue")
rotate(0, 0, 45)
rectangle(0, 0, 100, 50, "blue")
scale(0, 0, 2, 2)
rectangle(0, 0, 100, 50, "blue")

circle(100, 50, 50, "red")
circle(300,50,50,"red")
t.hideturtle()
turtle.exitonclick()