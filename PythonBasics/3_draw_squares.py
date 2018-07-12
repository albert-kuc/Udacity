import turtle


def draw_square(some_turtle):
    """ Method to draw a square """

    """ Draw square """
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_circle():
    """ Method to draw a circle """

    """ Initialise turtle and customize """
    milena = turtle.Turtle()
    milena.shape("arrow")
    milena.color('blue')
    milena.speed(2)

    """ Draw a circle """
    milena.circle(100)


def draw_triangle():
    """ Method to draw a triangle """

    """ Initialise turtle and customize """
    mario = turtle.Turtle()
    mario.shape("square")
    mario.color('red')
    mario.speed(2)

    """ Draw a triangle """
    for i in range(3):
        mario.right(120)
        mario.forward(150)


def draw_art():
    """ Initialise turtle and customize """
    mikele = turtle.Turtle()
    mikele.shape("turtle")
    mikele.color('green')
    mikele.speed(48)

    for i in range(36):
        draw_square(mikele)
        mikele.right(10)


""" Initialise window for output"""
window = turtle.Screen()
window.bgcolor("orange")

""" Call the methods """
# draw_square()
# draw_circle()
# draw_triangle()
draw_art()

""" Close window at onclick """
window.exitonclick()
