import turtle
colors = ['blue','orange','purple','white','red','green']
t = turtle.Turtle()
Screen = turtle.Screen()
Screen.bgcolor('Black')
t.speed(15)
for i in range(100):
    t.color(colors[i%6])
    t.fd(i*5)
    t.left(200)
    t.width(2)
turtle.exitonclick()