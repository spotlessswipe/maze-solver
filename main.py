from cell import Cell
from maze import Maze
from window import Window
import sys

sys.setrecursionlimit(10000)

def main():
    num_rows = 100
    num_cols = 100
    margin = 50
    screen_x = 1200
    screen_y = 1200
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 1)
    maze.solve()
    win.wait_for_close()

main()