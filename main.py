from line import Line
from point import Point
from window import Window

win = Window(800, 600)

line1 = Line(Point(0,300),Point(300, 0))
win.draw_line(line1, 'black')

win.wait_for_close()