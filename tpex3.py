import turtle

hexagon=turtle.Turtle()

hexagon.speed(2)

hexagon.shape("turtle")
hexagon.pensize(5)
size=int(input("enter the size of each side: "))
for steps in range(2):
    for c in ('blue', 'red', 'green'):
        hexagon.color(c)
        hexagon.forward(size)
        hexagon.left(60)
      
    

turtle.done()