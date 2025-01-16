import random as rand

#Start Message
print("Hello! This game is inspired by the game 'Shut The Box'. The goal is to roll 2 random numbers, and either combine or use them separately to remove certain values from the overall 'box' If you roll two numbers and they have already been used separately, and used if they were combined, you lose and need to restart.")

#List

total_values_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

#Random Dice Rolls
roll1 = rand.randint(1, 6)
roll2 = rand.randint(1, 6)

while True:
    play = input("Would you like to roll? (yes/no) ").strip().lower()
    if play == "no":
        print("Ok, nice playing with you!")
    elif play != "yes":
        print("Please type 'yes' or 'no'")
        continue



    choice = int(input("Do you want to have the numbers separate or combined? Type 1 for Sep, 2 for Comb"))



    if choice == 1:
     print("Ok, both of those numbers have been eliminated from the overall 12 numbers")
     total_values_list.remove(roll1)
     total_values_list.remove(roll2)
     print(total_values_list)

    elif choice == 2:
        print("Ok,the combined have been eliminated from the overall 12 numbers")
        combo_roll = roll1 + roll2
        total_values_list.remove(combined_roll())
        print(total_values_list)

    elif choice >= 3:
        print("Please choose either 1 for Sep, 2 for Comb")



