# Importing my own files
from graphics import Window, Point, Line

# Functions
def main():
    win = Window(800, 600)
    l = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l, "black")
    win.wait_for_close()


# Program starts here
if __name__ == "__main__":
    main()