import turtle as trtl
import random as rand
from typing import Tuple

# initialize variable

wn=trtl.Screen()
maze_painter = trtl.Turtle()
global length
length = 35
path_width = 30
maze_painter.left(90)
maze_painter.pensize(5)
maze_painter.speed(10)
door = rand.randint(path_width*2, (wall_len - path_width*2))
barrier = rand.randint(path_width*2, (wall_len - path_width*2))
barrier_limits = rand.randint(-100, 100)
# setup turtle

def barriers():
    global length
    if wall > 5:
        draw_barriers()
    maze_painter.forward(length - path_width - (length / 3))
    maze_painter.left(90)
    length += 15

def draw_barriers():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)
for wall in range(21):
    maze_painter.forward(length/3)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    barriers(barrier_limits)

wn.mainloop()

