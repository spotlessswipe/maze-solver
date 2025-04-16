from cell import Cell
from maze import Maze
from window import Window
import sys

sys.setrecursionlimit(3000)

def main():
    num_rows = 50
    num_cols = 50
    margin = 50
    screen_x = 1000
    screen_y = 1000
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 1)
    maze.solve()
    win.wait_for_close()

main()