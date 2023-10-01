# This file is Game.py created on 2023.09.29
import random
import Role1
import Role2

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



###############################################################################################

# these are the attributes of the actor playing the game
ActorRole = ""
ActorHealth = 0
ActorDexterity = 0
ActorIntelligence = 0
ActorCharisma	= 0
ActorCombat = 0

# stores: 1 for The Spy or 2 for The Thief. Error-0
TheActor = 0

# stores the current challenge
CurrentChallenge = 1

# stores the number of warnings
NoOfWarnings = 0

# returns the actor's health
def GetActorHealth():
    return ActorHealth

# returns the string of the actor
def GetTheCharacterRole():
    return ActorRole

# returns the number of warnings
def GetNoOfWarnings():
    return NoOfWarnings

# sets the number of warnings
def SetNoOfWarnings(NewWarnings):
    global NoOfWarnings
    NoOfWarnings = NewWarnings

# returns the games' current challenge
def GetCurrentChallenge():
    return CurrentChallenge;

# sets the game's current challenge
def SetCurrentChallenge(NewChallenge):
    global CurrentChallenge
    CurrentChallenge = NewChallenge

# sets the role of TheActor in the game
def SetTheActor (TheCharacter):
    global TheActor
    global ActorRole
    global ActorHealth
    global ActorDexterity 
    global ActorIntelligence
    global ActorCharisma
    global ActorCombat
    global NoOfWarnings
    global CurrentChallenge
    if TheCharacter == 1:
        TheActor = 1
        ActorRole = Role1.WhatIsYourCharacter()
        ActorHealth = Role1.WhatIsYourHealth()
        ActorDexterity = Role1.WhatIsYourDexterity()
        ActorIntelligence = Role1.WhatIsYourIntelligence()
        ActorCharisma	= Role1.WhatIsYourCharisma()
        ActorCombat = Role1.WhatIsYourCombat()
    elif TheCharacter == 2:
        TheActor = 2
        ActorRole = Role2.WhatIsYourCharacter()
        TheActor = Role2.WhatIsYourCharacter()
        ActorHealth = Role2.WhatIsYourHealth()
        ActorDexterity = Role2.WhatIsYourDexterity()
        ActorIntelligence = Role2.WhatIsYourIntelligence()
        ActorCharisma	= Role2.WhatIsYourCharisma()
        ActorCombat = Role2.WhatIsYourCombat()
    else:
        TheCharacter = 0
        ActorRole = "Invalid value for the Actor."
    NoOfWarnings = 0
    CurrentChallenge = 0


# retrieve the attributes of the character and returns a string
def GetTheCharacterAtributes():
    global TheActor
    global ActorRole
    global ActorHealth
    global ActorDexterity
    global ActorIntelligence
    global ActorCharisma
    global ActorCombat

    BuildTheString = " These are my attributes:\n"
    BuildTheString += " [ Health: " + str(ActorHealth)
    BuildTheString += "; Dexterity: " + str(ActorDexterity)
    BuildTheString += "; Intelligence: " + str(ActorIntelligence)
    BuildTheString += "; Charisma: " + str(ActorCharisma)
    BuildTheString += "; Combat: " + str(ActorCombat) + "]"
    return BuildTheString


def Challenge_1():
    global NoOfWarnings
    global ActorHealth
    NoOfWarnings += 1
    ActorHealth -= 1
    print("This is challenge 1")


def Challenge_2():
    global NoOfWarnings
    global ActorHealth
    NoOfWarnings += 1
    ActorHealth -= 1
    print("This is challenge 2")

def Challenge_3():
    global NoOfWarnings
    global ActorHealth
    NoOfWarnings += 1
    ActorHealth -= 1
    print("This is challenge 3")

def Challenge_4():
    global NoOfWarnings
    global ActorHealth
    NoOfWarnings += 1
    ActorHealth -= 1
    print("This is challenge 4")


