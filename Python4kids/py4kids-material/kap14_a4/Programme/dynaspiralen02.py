# Python für Kids (4. Auflage) - Kapitel 14
# Objekte und Methoden

# Autor: Gregor Lingl
# Datum: 20. 8. 2009
# dynaspiralen_arbeit.py

from turtle import Turtle, Screen

def jump(turtle, laenge):
    turtle.penup()
    turtle.forward(laenge)
    turtle.pendown()

def polyschritt(turtle, laenge, winkel):
    turtle.forward(laenge)
    turtle.left(winkel)


screen = Screen()

alex = Turtle()
bert = Turtle()
bert.left(90)
bert.color("red")
carl = Turtle()
carl.color("green")
carl.left(180)
dinu=Turtle()
dinu.left(270)
dinu.color("blue")
kroeten = (alex, bert, carl, dinu)

for krot in kroeten:
    krot.hideturtle()
    krot.speed(0)
    jump(krot, 50)
    krot.pensize(3)
    krot.right(30)
    
for laenge in range(100, 0, -5):
    screen.tracer(False)
    for krot in kroeten:
        polyschritt(krot, laenge, 120)
    screen.tracer(True)
