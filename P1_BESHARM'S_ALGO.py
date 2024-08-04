import turtle
def B_MAN(x1,y1,x2,y2):
    dx = abs(x1-x2)              # Calculating dx & dy
    dy = abs(y1-y2)

    step_x = 1 if x2>x1 else -1  # Determining step direction of each axis
    step_y = 1 if y2>y1 else -1

    error = 2*dx-dy             # Initializing error --> ((2*dx)-dy)
    l_p = []                    # Initializing Line_Points
    x,y = x1,y1
    for _ in range(dx+1):
        l_p.append((x,y))
        if error > 0:
            y += step_y
            error -= 2*dx
        error += 2*dy
        x += step_x
    return l_p

turtle.setup(500,500)
turtle.speed(0)
x1,y1 = 100,100
x2,y2 = 400,0
l_p = B_MAN(x1, y1, x2, y2)

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
for x,y in l_p:
    turtle.goto(x, y)
turtle.exitonclick()

