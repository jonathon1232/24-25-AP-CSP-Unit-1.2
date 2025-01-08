import random as rand

dice_numbers_list1 = ["1", "2", "3", "4", "5", "6"]
dice_numbers_list2 = ["1", "2", "3", "4", "5", "6"]
total_values_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

roll1 = rand.randint(0, len(dice_numbers_list1))
roll2 = rand.randint(0, len(dice_numbers_list1))

print(roll1)
print(roll2)
answer = int(input("Do you want those numbers out separate or combined? (sep./com.)"))
if answer == "sep.":
