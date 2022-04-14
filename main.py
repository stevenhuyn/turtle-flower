from svg_turtle import SvgTurtle
import math
import turtle
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PIL import Image
import os


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 14) + 1
    step_length = arc_length / n
    step_angle = angle / n

    # Making a slight left turn before starting
    # reduces the error caused by the linear approximation of the arc
    t.lt(step_angle / 2)

    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)


def circle(t, r):
    arc(t, r, 360)

def flower_petal(t, c, angle):
    radians = angle * math.pi / 180
    radius_of_arc = (c * math.sin((math.pi - radians) / (2))) / (math.sin(radians))
    arc(t, radius_of_arc, angle)
    t.lt(180 - angle)
    arc(t, radius_of_arc, angle)


def flower(t, c, angle, n):
    for i in range(n):
        turn = (i + 1) * 360 / n
        t.lt(turn)
        flower_petal(t, c, angle)
        t.rt(turn)
        t.lt(180 - angle)
    turtle.update()


if __name__ == "__main__":
    filename = "large"

    for mode in ["LightMode", "DarkMode"]:
        t = SvgTurtle(2000, 2000)

        if mode == "DarkMode":
            t.pencolor(1, 1, 1)
            t.getscreen().bgcolor("black")

        flower(t, 250, 340, 150)

        t.save_as(f"{filename}{mode}.svg")

        drawing = svg2rlg(f"{filename}{mode}.svg")
        renderPM.drawToFile(drawing, f"{filename}{mode}.png", fmt="PNG")

        # Manipulating opacity of png
        img = Image.open(f"{filename}{mode}.png")
        rgba = img.convert("RGBA")
        data = rgba.getdata()

        newData = []
        for (r, g, b, a) in data:
            if mode == "LightMode":
                newData.append((r, g, b, 255 - r))
            else:
                newData.append((r, g, b, r))

        rgba.putdata(newData)
        rgba.save(f"opacified{filename[0].capitalize() + filename[1:]}{mode}.png", "PNG")

        # Cleanup
        os.remove(f"{filename}{mode}.png")

        # If DarkMode redo svg to git rid of the background
        if mode == "DarkMode":
            t = SvgTurtle(1000, 1000)
            t.pencolor(1, 1, 1)
            flower(t, 250, 340, 150)
            t.save_as(f"{filename}{mode}.svg")

