import turtle

def draw_star(size,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(5):
        turtle.fd(size)
        turtle.right(144)
        
draw_star(20,40,20)
draw_star(50,80,40)
draw_star(120,140,60)
