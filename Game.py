# This file is Game.py created on 2023.09.29
import random
import Role1
import Role2

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


# returns True if the challenge is passed, False if it fails.
def pass_challenge(dificulty, dice, attribute, attribute_2):
    total_number = dice + attribute + attribute_2
    if total_number >= dificulty:
        return True
    else:
        return False

# Challange 1 runs here
def Challenge_1(user_choice, dice):
    roll = 1
    if user_choice == 1:
        pass_result = pass_challenge(5, dice, ActorDexterity, 0)
        return pass_result
    elif user_choice == 2:
        pass_result = pass_challenge(4, dice, ActorDexterity, 0)
        return pass_result
    elif user_choice == 3 and roll == 1:
        return True

# Challange 2 runs here
def Challenge_2(user_choice, dice):
    if user_choice == 1:
        pass_result = pass_challenge(5, dice, ActorCharisma, 0)
        return pass_result
    elif user_choice == 2:
        pass_result = pass_challenge(6, dice, ActorDexterity, 0)
        return pass_result
    elif user_choice == 3:
        return True

# Challange 3 runs here
def Challenge_3(user_choice, dice):
    if user_choice == 1:
        pass_result = pass_challenge(5, dice, ActorIntelligence, 0)
        return pass_result
    elif user_choice == 2:
        pass_result = pass_challenge(3, dice, ActorCombat, 0)
        return pass_result

# Challange 4 runs here
def Challenge_4(user_choice, dice):
    user_choice = 1
    if user_choice == 1:
        pass_result = pass_challenge(7, dice, ActorIntelligence, ActorDexterity)
        return pass_result

# Challange 5 runs here
def Challenge_5(user_choice, dice):
    if user_choice == 1:
        pass_result = pass_challenge(7, dice, ActorDexterity, 0)
        return pass_result
    elif user_choice == 2:
        pass_result = pass_challenge(6, dice, ActorCharisma, 0)
        return pass_result

# sets the role of TheActor in the game
def SetTheActor (TheCharacter):
    global TheActor
    global ActorRole
    global ActorHealth
    global ActorDexterity 
    global ActorIntelligence
    global ActorCharisma
    global ActorCombat

    SetNoOfWarnings(0)
    SetCurrentChallenge(1)

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
 

# retrieve the attributes of the character and returns a string
def GetTheCharacterAtributes():
    BuildTheString = " These are my attributes:\n"
    BuildTheString += " [ Health: " + str(ActorHealth)
    BuildTheString += "; Dexterity: " + str(ActorDexterity)
    BuildTheString += "; Intelligence: " + str(ActorIntelligence)
    BuildTheString += "; Charisma: " + str(ActorCharisma)
    BuildTheString += "; Combat: " + str(ActorCombat) + "]"
    return BuildTheString

