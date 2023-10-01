# This file is Game.py created on 2023.09.29
import random
#steal migufin that is in a vault
# pick Spy, Theif, Bounty hunter
#each will hav 1 uniqe chalenge 
#but will share the rest
#stats are (Constitution, strength, dexterity, intelignece, chrisma, wisdom)
#start at the ficility where the vault is
#choose what time to start the raid (morning, noon, afternoon, night)
#get into building
#dont get caught by gaurds
#find location of the vault
#get the vault code/get into the vault
#find the migufin
#get out of the building
#dont get caught by police
#make it back to homebase

def Number_check(find_int):
    if find_int.isnumeric() == True:
        return True
    else:
        return False

def Number_chioce(Choice_posible):
    while True:
        user_selection = input("Please input the coresponding number to the chouice you want to make: ")
        is_number = Number_check(user_selection)
        if Number_check(is_number) == True:
            is_number = int(is_number)
            if is_number == 1 and Choice_posible >= 1:
                return 1
            elif is_number == 2 and Choice_posible >= 2:
                return 2
            elif is_number == 3 and Choice_posible >= 3:
                return 3
            else:
                print("Please input a proper selection")

#def time_of_day():
#    print("What time do you choose to start your raid\n"
#          "keep in mind that the more time you wait the higher the chance of guards hearing about the raid")
#    while True


def dice_role(x):
    dice_total = 0
    while x >= 1:
        dice_result = random.randrange(1,6)
        dice_total = dice_total + dice_result
        x = x - 1
    return dice_total

def pass_challenge(dificulty, dice_count, attribute, attribute_2):
    dice_total = dice_role(dice_count)
    total_number = dice_total + attribute + attribute_2
    if total_number >= dificulty:
        return True
    else:
        return False

def challenge_1():
    print("challenge 1")
    print("Sneak in on an army vehicle ")
    print("Climb building and enter the vents")
    print("Main entrance")
    user_choice = Number_chioce(3)
    if user_choice == 1:
        pass_result = pass_challenge(5, 1, attribute, 0)
        return pass_result
    elif user_choice == 2:
        pass_result = pass_challenge(4, 1, attribute, 0)
        return pass_result
    elif user_choice == 3 and roll == 1:
        return True

def challenge_2():
    print("challenge 2")
    print("Bluff past ")
    print("Sneak past")
    print("Suprise attack")
    user_choice = Number_chioce(3)
    if user_choice == 1:
        pass_result = pass_challenge(5, 1, attribute, 0)
        return pass_result
    elif user_choice == 2:
        pass_result = pass_challenge(6, 1, attribute, 0)
        return pass_result
    elif user_choice == 3:
        return True

def challenge_3():
    print("challenge 3")
    print("Ask the head scientist for location")
    print("intimidate head scientist")
    user_choice = Number_chioce(2)
    if user_choice == 1:
        pass_result = pass_challenge(5, 1, attribute, 0)
        return pass_result
    elif user_choice == 2:
        pass_result = pass_challenge(3, 1, attribute, 0)
        return pass_result

def challenge_4():
    print("challenge 4")
    print("unlock vault")
    user_choice = Number_chioce(1)
    if user_choice == 1:
        pass_result = pass_challenge(7, 1, attribute, attribute_2)
        return pass_result

def challenge_5():
    print("challenge 5")
    print("sneak out")
    print("bluff past")
    user_choice = Number_chioce(2)
    if user_choice == 1:
        pass_result = pass_challenge(7, 1, attribute, 0)
        return pass_result
    elif user_choice == 2:
        pass_result = pass_challenge(6, 1, attribute, 0)
        return pass_result
