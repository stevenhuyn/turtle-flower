from svg_turtle import SvgTurtle
import math
import turtle
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PIL import Image, ImageGrab, ImageOps
import os
import tkinter as tk


class FlowerDrawer:
    def __init__(self, fidelity: float, width: int, height: int, initialLeftTurn: bool):
        self.fidelity = fidelity
        self.width = width
        self.height = height
        self.initialLeftTurn = initialLeftTurn
        self.c = 240
        self.angle = 300
        self.n = 300

    def setFlowerArgs(self, c, angle, n):
        self.c = c
        self.angle = angle
        self.n = n

    def polyline(self, t, n, length, angle):
        for i in range(n):
            t.fd(length)
            t.lt(angle)

    def arc(self, t, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / self.fidelity) + 1
        step_length = arc_length / n
        step_angle = angle / n

        # Making a slight left turn before starting
        # reduces the error caused by the linear approximation of the arc
        # Creates interesting effercts
        if self.initialLeftTurn:
            t.lt(step_angle / 2)

        self.polyline(t, n, step_length, step_angle)
        t.rt(step_angle / 2)

    def flower_petal(self, t, c, angle):
        radians = angle * math.pi / 180
        radius_of_arc = (c * math.sin((math.pi - radians) / (2))) / (math.sin(radians))
        self.arc(t, radius_of_arc, angle)
        t.lt(180 - angle)
        self.arc(t, radius_of_arc, angle)

    def flower(self, t, c, angle, n):
        for i in range(n):
            turn = (i + 1) * 360 / n
            t.lt(turn)
            self.flower_petal(t, c, angle)
            t.rt(turn)
            t.lt(180 - angle)
        turtle.update()

    def svgTurtle(self, filename: str):
        for mode in ["LightMode", "DarkMode"]:
            t = SvgTurtle(1000, 1000)

            if mode == "DarkMode":
                t.pencolor(1, 1, 1)
                t.getscreen().bgcolor("black")

            self.flower(t, self.c, self.angle, self.n)

            t.save_as(f"{filename}{mode}.svg")

            drawing = svg2rlg(f"{filename}{mode}.svg")
            renderPM.drawToFile(drawing, f"{filename}{mode}.png", fmt="PNG")

            self.opacifiy(f"{filename}{mode}.png")

            # If DarkMode redo svg to git rid of the background
            if mode == "DarkMode":
                t = SvgTurtle(1000, 1000)
                t.pencolor(1, 1, 1)
                self.flower(t, self.c, self.angle, self.n)
                t.save_as(f"{filename}{mode}.svg")

    def opacifiy(self, filename, mode):
        # Manipulating opacity of png
        img = Image.open(filename)
        rgba = img.convert("RGBA")
        data = rgba.getdata()

        newData = []
        for (r, g, b, a) in data:
            if mode == "LightMode":
                newData.append((r, g, b, 255 - r))
            else:
                newData.append((r, g, b, r))

        rgba.putdata(newData)
        rgba.save(f"opacified{filename[0].capitalize() + filename[1:]}.png", "PNG")

        # Cleanup
        # os.remove(f"{filename}{mode}.png")

    def regularTurtle(self, filename: str, lightMode=True):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1000, height=1000)
        canvas.pack()

        t = turtle.RawTurtle(canvas)
        t.speed("fastest")
        if not lightMode:
            t.pencolor("white")
            t.getscreen().bgcolor("black")
        # t.pu()
        # t.goto(1080 / 4, 0)
        # t.pd()
        # Inward style (double layer) c > 180, c doens't make sense here
        t.getscreen().tracer(0, 0)
        # ts = turtle.getscreen()
        ##ts.getcanvas().postscript(file="duck.eps")

        self.flower(t, self.c, self.angle, self.n)
        t.hideturtle()
        self.dump_gui(root, filename)

    def dump_gui(self, root, filename):
        """
        takes a png screenshot of a tkinter window, and saves it on in cwd
        """
        print("...dumping gui window to png")

        x0 = root.winfo_rootx()
        y0 = root.winfo_rooty()
        x1 = x0 + root.winfo_width()
        y1 = y0 + root.winfo_height()
        print(x0, y0, x1, y1)
        ImageGrab.grab().crop((x0, y0, x1, y1)).save(f"{filename}.png")


if __name__ == "__main__":
    fd = FlowerDrawer(3, 1000, 1000, True)
    fd.setFlowerArgs(240, 300, 300)

    fd.regularTurtle("ScaryLight", True)
    fd.opacifiy("ScaryLight.png", "LightMode")

    fd.regularTurtle("ScaryDark", False)
    fd.opacifiy("ScaryDark.png", "DarkMode")
