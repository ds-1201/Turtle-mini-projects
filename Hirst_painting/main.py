# import colorgram
#
# colors = colorgram.extract('dot_painting.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)
import turtle as t
import random

t.colormode(255)
painter = t.Turtle()
screen = t.Screen()
painter.penup()

colors_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]


def painting():
    x_pos = -325
    y_pos = -250
    painter.goto(x_pos, y_pos)
    for i in range(12):
        for _ in range(14):
            color = random.choice(colors_list)
            painter.dot(20, color)
            painter.fd(50)
        y_pos = y_pos+50
        painter.goto(x_pos, y_pos)


painting()

screen.exitonclick()