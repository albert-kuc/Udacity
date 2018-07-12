import turtle


def draw_square():
    """ Method to draw a square """

    """ Initialise turtle and customize """
    mikele = turtle.Turtle()
    mikele.shape("turtle")
    mikele.color('green')
    mikele.speed(2)

    """ Draw square """
    for i in range(4):
        mikele.forward(100)
        mikele.right(90)




def draw_circle():
    """ Method to draw a circle """

    """ Initialise turtle and customize """
    milena = turtle.Turtle()
    milena.shape("arrow")
    milena.color('blue')
    milena.speed(2)

    """ Draw a circle """
    milena.circle(100)


""" Initialise window for output"""
window = turtle.Screen()
window.bgcolor("orange")

""" Call the methods """
draw_square()
draw_circle()

""" Close window at onclick """
window.exitonclick()
