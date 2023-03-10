import turtle
a=turtle.Turtle()
screen=turtle.Screen().bgcolor('black')
col=('white','orange','red','yellow','green','cyan','blue')
a.speed(0)
for i in range(200):
    a.forward(i*4)
    a.right(91)
    a.color('orange')
    for b in range(3):
        a.forward(i*4)
        a.right(91)
        for c in range(2):
            a.forward(i*4)
            a.right(91)

