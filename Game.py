# This file is Game.py created on 2023.09.29
# import all modules needed 
import random
import TheSpy
import TheThief

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
def pass_challenge(difficulty, dice, attribute_1, attribute_2):
    total_number = dice + attribute_1 + attribute_2
    if total_number >= difficulty:
        return True
    else:
        return False

# Challange 1: enter the base. runs here
def Challenge_1_EnterBase(user_choice, dice):
    # constants for difficulty 
    Difficutly_5 = 5
    Difficutly_4 = 4
    if user_choice == 1:
#
        pass_result = pass_challenge(Difficutly_5, dice, ActorDexterity, 0)
    elif user_choice == 2:
        pass_result = pass_challenge(Difficutly_4, dice, ActorDexterity, 0)
    elif user_choice == 3:
# pass for the spy due to working there
        if TheActor== 1:
           pass_result = True
        elif TheActor== 2:
           pass_result = False
    return pass_result

# Challange 2: evade the gaurds. runs here
def Challenge_2_EvadeGuards(user_choice, dice):
    Difficutly_5 = 5
    Difficutly_6 = 6
    if user_choice == 1:
        pass_result = pass_challenge(Difficutly_5, dice, ActorCharisma, 0)
    elif user_choice == 2:
        pass_result = pass_challenge(Difficutly_6, dice, ActorDexterity, 0)
    elif user_choice == 3:
        pass_result = pass_challenge(Difficutly_5, dice, ActorCombat, 0)
    return pass_result

# Challange 3: Find the vault. runs here
def Challenge_3_FindVault(user_choice, dice):
    Difficutly_5 = 5
    Difficutly_3 = 3
    if user_choice == 1:
        pass_result = pass_challenge(Difficutly_5, dice, ActorIntelligence, 0)
    elif user_choice == 2:
        pass_result = pass_challenge(Difficutly_3, dice, ActorCombat, 0)
    return pass_result

# Challange 4: open the vault. runs here
def Challenge_4_OpenVault(user_choice, dice):
    Difficutly_7 = 7
    user_choice = 1
    if user_choice == 1:
        pass_result = pass_challenge(Difficutly_7, dice, ActorIntelligence, ActorDexterity)
    elif user_choice == 2:
        pass_result = pass_challenge(Difficutly_7, dice, ActorIntelligence, ActorDexterity)    
    return pass_result

# Challange 5: Escape enemy base. runs here
def Challenge_5_EscapeBase(user_choice, dice):
    Difficutly_7 = 7
    Difficutly_6 = 6
    if user_choice == 1:
        pass_result = pass_challenge(Difficutly_7, dice, ActorDexterity, 0)
    elif user_choice == 2:
        pass_result = pass_challenge(Difficutly_6, dice, ActorCharisma, 0)
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
#sets the player character states equal to the spy
    if TheCharacter == 1:
        TheActor = 1
        ActorRole = TheSpy.WhatIsYourCharacter()
        ActorHealth = TheSpy.WhatIsYourHealth()
        ActorDexterity = TheSpy.WhatIsYourDexterity()
        ActorIntelligence = TheSpy.WhatIsYourIntelligence()
        ActorCharisma	= TheSpy.WhatIsYourCharisma()
        ActorCombat = TheSpy.WhatIsYourCombat()
#sets the player character states to the Thief
    elif TheCharacter == 2:
        TheActor = 2
        ActorRole = TheThief.WhatIsYourCharacter()
        TheActor = TheThief.WhatIsYourCharacter()
        ActorHealth = TheThief.WhatIsYourHealth()
        ActorDexterity = TheThief.WhatIsYourDexterity()
        ActorIntelligence = TheThief.WhatIsYourIntelligence()
        ActorCharisma	= TheThief.WhatIsYourCharisma()
        ActorCombat = TheThief.WhatIsYourCombat()
#repeat until proper input is given
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

# Increases the warning count by 1 if the player failed
def UpdateWarningCount(pass_result):
    global NoOfWarnings
    if pass_result == False:
        NoOfWarnings += 1

    return NoOfWarnings
