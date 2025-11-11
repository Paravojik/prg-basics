import turtle
import random
def draw_square(pen,length):
    pen.penup()
    pen.goto(random.randint(-400,400-int(length)),random.randint(-300,300-int(length)))
    pen.pendown()
    for i in range(4):
        pen.forward(length)
        pen.right(90)
def draw_triangle(pen,length):
    pen.penup()
    pen.goto(random.randint(-400,400-int(length)),random.randint(-300,300-int(length)))
    pen.pendown()
    for i in range(3):
        pen.forward(length)
        pen.right(120)
def draw_rectangle(pen,length_a,length_b):
    pen.penup()
    pen.goto(random.randint(-400,400-int(length_a)),random.randint(-300,300-int(length_b)))
    pen.pendown()
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)