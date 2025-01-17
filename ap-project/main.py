import random as rand

#Start Message
print("Hello! This game is inspired by the game 'Shut The Box'. The goal is to roll 2 random numbers, and either combine or use them separately to remove certain values from the overall 'box' If you roll two numbers and they have already been used separately, and used if they were combined, you lose and need to restart.")

#List
total_values_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

#Checking if the rolled number is in the list or not
def is_valid_choice(choice):
    return choice in total_values_list

#cited from chatgpt
while True:
    if not total_values_list:
        print("Congrats! You used all numbers!")
        break

    #Dice rolls
    roll1 = rand.randint(1, 6)
    roll2 = rand.randint(1, 6)


    play = input("Would you like to roll? (yes/no) ").strip().lower()
    if play == "no":
        print("Ok, nice playing with you!")
        break
    elif play != "yes":
        print("Please type 'yes' or 'no'")
        continue

    print(f"You rolled: {roll1}, {roll2}")
#end citation
    choice = input("Do you want to have the numbers separate (1) or combined (2)?").strip()


    #Making both numbers you rolled taken out of the list if you chose separate.
    if choice == "1":
        if is_valid_choice(str(roll1)) and is_valid_choice(str(roll2)):
            print("Ok, both of those numbers have been eliminated from the overall 12 numbers")
            total_values_list.remove(str(roll1))
            total_values_list.remove(str(roll2))
            print(total_values_list)
        else:
            print("One of those numbers has been used already! You lose and need to restart!)")

    #Making both numbers be added into a sum, and the sum is taken out of the list if you chose combined.
    elif choice == "2":
        combo_roll = roll1 + roll2
        if is_valid_choice(str(combo_roll)):
            print(f"Ok,the combined number {combo_roll}have been eliminated from the overall 12 numbers")
            total_values_list.remove(str(combo_roll))
            print("Remaining values:", total_values_list)
        else:
            print("The combined number {combo_roll} has been used already!")
    #failsafe incase you don't pick one of the numbers.
    else:
        print("Please type '1' or '2'")


