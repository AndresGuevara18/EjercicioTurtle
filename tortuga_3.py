import turtle

#ventana
screen = turtle.Screen()
screen.title("LABRINTO CON TURTLE")
screen.bgpic('laberinto_22.gif')

#instancia tortuga
tortuga = turtle.Turtle()
tortuga.shape('turtle')
tortuga.shapesize(stretch_wid=1.2, stretch_len=1.2)
tortuga.penup()
tortuga.goto(-20, 0)
tortuga.pendown()
tortuga.speed(8)

for i in range (1,6):
    if i == 1:
        tortuga.left(50)
        tortuga.forward(135)
        tortuga.color("red")
        tortuga.right(90)
        tortuga.circle(-130, 40)
        #vuelta
        tortuga.left(180)
        tortuga.circle(130, 40)
    elif i == 2:
        tortuga.color("black")
        tortuga.circle(170, 25)
        tortuga.right(85)
        tortuga.forward(30)
        tortuga.left(90)
        tortuga.circle(160, 70)
        tortuga.right(90)
        tortuga.forward(25)
        tortuga.right(90)
        tortuga.circle(-187, 95)    
    elif i == 3:
        tortuga.color("red")
        tortuga.left(90)
        tortuga.forward(27)
        tortuga.left(90)
        tortuga.circle(215, 48)
        #vuelta
        tortuga.left(180)
        tortuga.circle(-215, 48)
        tortuga.right(90)
        tortuga.forward(27)
    elif i == 4:
        tortuga.color("black")
        tortuga.left(90)
        tortuga.circle(-188, 137)
        #
        tortuga.color("red")
        tortuga.circle(-188, 40)
        tortuga.left(180)
        tortuga.circle(188, 40)
        tortuga.right(90)
        #
        tortuga.color("black")
        tortuga.forward(27)
    else:
        tortuga.left(90)
        tortuga.color("red")
        tortuga.circle(208, 48)
        tortuga.left(180)
        tortuga.circle(-208, 48)

        tortuga.color("black")
        tortuga.circle(-208, 45)
        tortuga.left(90)
        tortuga.forward(40)
        tortuga.color("green")

        for i in range (360):
            #tortuga.forward(1/2)
            tortuga.right(7)
    print(i)
"""#1
tortuga.left(50)
tortuga.forward(135)
tortuga.color("red")
tortuga.right(90)
tortuga.circle(-130, 40)
#vuelta
tortuga.left(180)
tortuga.circle(130, 40)

#2
tortuga.color("black")
tortuga.circle(170, 25)
tortuga.right(85)
tortuga.forward(30)
tortuga.left(90)
tortuga.circle(160, 70)
tortuga.right(90)
tortuga.forward(25)
tortuga.right(90)
tortuga.circle(-187, 95)

#3
tortuga.color("red")
tortuga.left(90)
tortuga.forward(27)
tortuga.left(90)
tortuga.circle(215, 48)
#vuelta
tortuga.left(180)
tortuga.circle(-215, 48)
tortuga.right(90)
tortuga.forward(27)
#4
tortuga.color("black")
tortuga.left(90)
tortuga.circle(-188, 137)
#
tortuga.color("red")
tortuga.circle(-188, 40)
tortuga.left(180)
tortuga.circle(188, 40)
tortuga.right(90)
#
tortuga.color("black")
tortuga.forward(27)

#5
tortuga.left(90)
tortuga.color("red")
tortuga.circle(208, 48)
tortuga.left(180)
tortuga.circle(-208, 48)

tortuga.color("black")
tortuga.circle(-208, 45)
tortuga.left(90)
tortuga.forward(40)
tortuga.color("green")

for i in range (360):
    #tortuga.forward(1/2)
    tortuga.right(7)"""





turtle.done()