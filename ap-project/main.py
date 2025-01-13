import random as rand

dice_numbers_list1 = ["1", "2", "3", "4", "5", "6"]
dice_numbers_list2 = ["1", "2", "3", "4", "5", "6"]
total_values_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

roll1 = rand.randint(0, len(dice_numbers_list1))
roll2 = rand.randint(0, len(dice_numbers_list1))


print(roll1)
print(roll2)

# cited from https://www.bing.com/search?pglt=43&q=how+to+rempove+random+vaues+from+a+list+in+python&cvid=36bf1af3854a42f081b2d6f6106f2c41&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOdIBCTEyMTE2ajBqMagCCLACAQ&FORM=ANSPA1&PC=U531
# term: how to rempove random vaues from a list in python
def remove_random_values():
    for num in range(6):
        value_to_remove = rand.choice(dice_numbers_list1)
        dice_numbers_list1.remove(value_to_remove)
        dice_numbers_list1.remove(value_to_remove)
# End Citation


choice = int(input("Do you want to have the numbers separate or combined? Type 1 for Sep, 2 for Comb"))

if choice == 1:
    remove_random_values()
    print(dice_numbers_list1)
