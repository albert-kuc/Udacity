import turtle

def draw_square():
    """ Method to draw a square """

    """ Initialise window for output"""
    window = turtle.Screen()
    window.bgcolor("orange")

    """ Initialise turtle """
    mikele = turtle.Turtle()

    """ Draw square """
    for i in range(4):
        mikele.forward(100)
        mikele.right(90)

    """ Close window at onclick """
    window.exitonclick()


draw_square()
