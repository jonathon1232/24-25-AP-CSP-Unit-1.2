# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
score_writer = trtl.Turtle()

#-----game functions--------
score_writer.penup()
score_writer.goto(0,200)
def spot_clicked(x, y):
   change_position(x, y)
   update_score()
def change_position(x, y):
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.penup()
    spot.goto(new_xpos, new_ypos)
    spot.penup()
def update_score():
    global score
    score += 1
    score_writer.write(score, font=font_setup)



#-----events------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()