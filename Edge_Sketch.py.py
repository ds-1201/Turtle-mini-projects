import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.fd(10)

def move_backward():
    tim.backward(10)

def move_left():
    angle = tim.heading()
    tim.setheading(angle+10)

def move_right():
    angle = tim.heading()
    tim.setheading(angle-10)

def reset_screen():
    screen.resetscreen()

screen.listen()
screen.onkeypress(fun=move_forward, key="Up")
screen.onkeypress(fun=move_backward, key="Down")
screen.onkeypress(fun=move_left, key="Left")
screen.onkeypress(fun=move_right, key="Right")
screen.onkeypress(fun=reset_screen, key="c")
screen.exitonclick()