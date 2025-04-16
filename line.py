from tkinter import Canvas

from point import Point


class Line:
    def __init__(self, point1: Point, point2: Point):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas: Canvas, fill_color: str = 'black'):
        canvas.create_line(
            self.__point1.x,
            self.__point1.y,
            self.__point2.x,
            self.__point2.y,
            fill=fill_color,
            width=2
        )

