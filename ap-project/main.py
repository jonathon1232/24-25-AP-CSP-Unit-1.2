import random as rand

#Start Message
print("Hello! This game is inspired by the game 'Shut The Box'. The goal is to roll 2 random numbers, and either combine or use them separately to remove certain values from the overall 'box' If you roll two numbers and they have already been used separately, and used if they were combined, you lose and need to restart.")

#Lists
dice_numbers_list1 = ["1", "2", "3", "4", "5", "6"]
dice_numbers_list2 = ["1", "2", "3", "4", "5", "6"]
total_values_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

#Random Dice Rolls
roll1 = dice_numbers_list1.pop(rand.randint(0, 5))
roll2 = dice_numbers_list2.pop(rand.randint(0, 5))

print(roll1)
print(roll2)

#Asking if your roll should be used combined or not
choice = int(input("Do you want to have the numbers separate or combined? Type 1 for Sep, 2 for Comb"))
if choice == 1:
    print("Ok, both of those numbers have been eliminated from the overall 12 numbers")
