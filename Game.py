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



x = input("thing:")
Number_chioce(x)


def Choose_role():




#def time_of_day():
    print("What time do you choose to start your raid\n"
          "keep in mind that the more time you wait the higher the chance of guards hearing about the raid")
#    while True

    


def dice_role(x):
    dice_total = 0
    while x >= 1:
        dice_result = random.randrange(1,6)
        dice_total = dice_total + dice_result
        x = x - 1
    return dice_total

x = int(input("Please input the number of dice you want to roll: "))

dice_test = dice_role(x)

print(dice_test)
print("how would you like to enter the bulding")
    


def challenge_1():
    print("challenge 1")





def challenge_2():
    print("challenge 2")






def challenge_3():
    print("challenge 3")






def challenge_4():
    print("challenge 4")

      