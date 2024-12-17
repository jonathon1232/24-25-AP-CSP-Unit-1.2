#Leaderboard Setup


# return names in the leaderboard file
def get_names(file_name):
    leaderboard_file = open(file_name, "r")  # be sure you have created this

    # use a for loop to iterate through the content of the file, one line at a time
    # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
    names = []
    for line in leaderboard_file:
        leader_name = ""
        index = 0

        # read leader name
        while (line[index] != ","):
            leader_name = leader_name + line[index]
            index = index + 1

        #add names
        names.append(leader_name)
    print("names:", names)

    leaderboard_file.close()


    return names


# return scores from the leaderboard file
def get_scores(file_name):
    leaderboard_file = open(file_name, "r")  # be sure you have created this

    scores = []
    for line in leaderboard_file:
        leader_score = ""
        index = 0


        while (line[index] != ","):
            index = index + 1
        index = index + 1


        while (line[index] != "\n"):
            leader_score = leader_score + line[index]
            index = index + 1


        scores.append(int(leader_score))
    print("scores:", scores)
    leaderboard_file.close()


    return scores


# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):
    index = 0
    for index in range(len(leader_scores)):
      if (player_score >= leader_scores[index]):
        break
      else:
        index = index + 1


    #gather player names
    leader_scores.insert(index, player_score)
    leader_names.insert(index, player_name)

    # 5 spots only
    if (len(leader_names) > 5):
        leader_names.pop(5)
        leader_scores.pop(5)

    # put file back

    leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
    for index in range(len(leader_names)): # note:can use scores list in place of names
      leaderboard_file.write(leader_names[index] + "," + str(leader_scores[index]) + "\n")

    leaderboard_file.close()


# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
    # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-160, 100)
    turtle_object.hideturtle()
    turtle_object.down()
    index = 0

    # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
    while (index < len(leader_names)):
        turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]),
                            font=font_setup)
        turtle_object.penup()
        turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
        turtle_object.down()
        index = index + 1

    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()

    # Did you make the leaderboard
    if player_score >= high_scorer:
        turtle_object.write("Good Job!\nYou made the leaderboard!", font=font_setup)
    else:
         turtle_object.write("Sorry!\nYou didn't make the leaderboard.", font=font_setup)


    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()

