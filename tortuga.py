import turtle

# Configurar la pantalla
screen = turtle.Screen()
screen.title("Laberinto con Turtle")
screen.bgcolor("black")#color fondo
screen.setup(1000, 700)

# Crear instancia de Turtle
tortuga = turtle.Turtle()
tortuga.shape('turtle')
tortuga.color('white')#color 
tortuga.speed(8)# Velocidad máxima
#tortuga.width()#ancho linea


for i in range (1, 6):
    if i == 1:
        tortuga.forward(30)
        tortuga.circle(60, 90)
        tortuga.left(90)
        tortuga.forward(90)
        tortuga.circle(80, 180)
        tortuga.forward(90)
        tortuga.left(90)
        tortuga.circle(60, 90)
        tortuga.forward(30)
    elif i == 2:
        tortuga.left(180)
        tortuga.forward(30)
        tortuga.circle(-60, 90)
        tortuga.right(90)
        tortuga.forward(90)
        tortuga.circle(-80, 90)
    elif i == 3:
        tortuga.left(90)
        tortuga.forward(30)
        tortuga.left(90)
        tortuga.circle(-80, 90)
        tortuga.forward(90)
        tortuga.right(90)
        tortuga.circle(-60, 90)
        tortuga.forward(30)
    elif i == 4:
        tortuga.right(180)
        tortuga.forward(30)
        tortuga.circle(60, 90)
        tortuga.left(90)
        tortuga.forward(90)
    else:
        tortuga.circle(80, 180)
        tortuga.forward(90)
        tortuga.left(90)
        tortuga.circle(60, 90)
        tortuga.forward(30)      
    print(i)

"""#1
tortuga.forward(30)
tortuga.circle(60, 90)
tortuga.left(90)
tortuga.forward(90)
tortuga.circle(80, 180)
tortuga.forward(90)
tortuga.left(90)
tortuga.circle(60, 90)
tortuga.forward(30)
#2 de vuelta
tortuga.left(180)
tortuga.forward(30)
tortuga.circle(-60, 90)
tortuga.right(90)
tortuga.forward(90)
tortuga.circle(-80, 90)

#3 otro
tortuga.left(90)
tortuga.forward(30)
tortuga.left(90)
tortuga.circle(-80, 90)
tortuga.forward(90)
tortuga.right(90)
tortuga.circle(-60, 90)
tortuga.forward(30)
#4
tortuga.right(180)
tortuga.forward(30)
tortuga.circle(60, 90)
tortuga.left(90)
tortuga.forward(90)
#5
tortuga.circle(80, 180)
tortuga.forward(90)
tortuga.left(90)
tortuga.circle(60, 90)
tortuga.forward(30)

#tortuga.circle(80,  steps = 5)"""




turtle.done()