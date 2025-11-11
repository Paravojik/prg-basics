import turtle
import figures
# Set up the screen
window = turtle.Screen()
window.setup(width=800, height=600)

window.bgcolor("lightgreen")
print(window.window_width(), window.window_height())
# Create the turtle
pen = turtle.Turtle()
pen.color("red")
pen.speed(5)
# Side length
side_length = int(input("Enter the side length of the square: "))

# Draw a square
for i in range(2):
    figures.draw_square(pen, side_length)
    figures.draw_triangle(pen, side_length)
    figures.draw_rectangle(pen, side_length,side_length*0.6)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()