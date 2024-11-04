# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
score_writer = trtl.Turtle()
counter =  trtl.Turtle()

font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----game functions--------
score_writer.penup()
score_writer.goto(0,300)
counter.penup()
counter.goto(300,300)
def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
        update_score()
        change_position(x, y)
    else:
        counter.penup()

def change_position(x, y):
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.penup()
    spot.goto(new_xpos, new_ypos)
    spot.penup()
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)




#-----events------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()