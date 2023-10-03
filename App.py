#This is the App.py file. Created 2023.09.29

# This file implements the interaction with the user.
# Sends the user's input to the game engine.

import Game
import random

# this is the welcome string
WelcomeMessage = "Welcome to SAVE THE WORLD adventure! This is a text based game.\n"

# this is the goodbye message
GoodbyeMessage = "The Game will terminate now.\nGoodbye!"

# this is the backgroud story of the game
ThisIsTheStory = """
    --------------------------------------------------------------------------------------------\n
    An enemy nation has developed a bioweapon that is able to infect and wipe out an entire city
    in just a few days. You are ordered to steal a sample of the bioweapon and the cure from the
    secret underground laboratory located in a military base. 
    There will be a 24-hour window where both the cure and weapon will be in the same vault.\n
    Only one person can go in to avoid suspicion. You can be:
    <The Spy>: you have been undercover as a scientist for many years and have an entrance pass key.\n
    <The Thief>: you are the greatest thief with great skils and the experience of many successful
                 heists. Also, you have a gun.\n
    --------------------------------------------------------------------------------------------\n"""
# this is the character's options
TheseAreTheRoles = """Would you like to be <The Spy> or the <The Thief>.
            Enter 1 for <The Spy>
            Enter 2 for <The Thief>"""

# number of options for challenge 1
OptionsForChallenge_1 = 3
# list the options for challange 1
MenuChallege_1_InfiltrateBase = """
      Challenge 1: Infiltrate Base _____________________
      <1> Sneak in on an army vehicle
      <2> Climb building and enter the vents
      <3> Main entrance"""

# number of options for challenge 2
OptionsForChallenge_2 = 3
# list the options for challange 2
MenuChallege_2_EvadeGuards = """
      Challenge 2: Evade Guards ________________________
      <1> Bluff past 
      <2> Sneak past
      <3> Suprise attack"""

# number of options for challenge 3
OptionsForChallenge_3 = 2
# list the options for challange 3
MenuChallege_3_FindVault= """
      Challenge 3: Find Vault __________________________
      <1> Ask the head scientist for location
      <2> Intimidate head scientist"""

# number of options for challenge 4
OptionsForChallenge_4 = 2
# list the options for challange 4
MenuChallege_4_OpenVault = """
      Challenge 4: Open Vault __________________________
      <1> Open vault with code
      <2> Open vault with skills"""

# number of options for challenge 5
OptionsForChallenge_5 = 2
# list the options for challange 5
MenuChallege_5_EscapeBase = """
      Challenge 5: Escape Base _________________________
      <1> Sneak out
      <2> Bluff past"""

# the user is choosing to play the game or exit
def StartMenu():
      while True:
            menu_start = input("Would you like to start the game (y/n): ")
            if menu_start == "y" or  menu_start == "Y" or  menu_start == "Yes":
                  return True  
            elif menu_start == "n" or  menu_start == "N" or  menu_start == "No": 
                  print(GoodbyeMessage)
                  exit()
            else:
                  print("Please enter: <Y> for Yes or <N> for No")

# the user selects the character to play
def CharacterMenu():
      while True:
            print(TheseAreTheRoles)
            menu_start = input("What would you like to be?: ")
            if menu_start == "1":
                  return 1  
            elif menu_start == "2":
                  return 2
            elif menu_start == "q":
                  print(GoodbyeMessage)
                  exit()
            else:
                  print("Please enter: <1> for The Spy or <2> for The Thief. [q - quit]")                  

# the user selects the option
def SelectionMenu(max_posible):
    while True:        
        if max_posible == 2:
            print("You can choose 1 or 2")
            menu_start = input("What is your selection?  ")
            if menu_start == "1":
                return 1  
            elif menu_start == "2":
                return 2
            elif menu_start == "q":
                exit()
            else:
                print("Please enter: <1> or <2> ") 
        else: 
            print("You can choose 1, 2 or 3")
            menu_start = input("What is your selection?  ")
            if menu_start == "1":
                return 1  
            elif menu_start == "2":
                return 2
            elif menu_start == "3":
                return 3
            elif menu_start == "q":
                exit()
            else:
                print("Please enter: <1>, <2> or <3>") 



def FailWarningMessage():
    NoOfWarning = Game.GetNoOfWarnings()
    if NoOfWarning == 3:
        print("to do")
        

# pause until the Enter key is pressed
def PressEnterToContinuue():
      WaitHere = input("Press <Enter> to continue")

# roll the dice
def RollTheDice():
      WaitHere = input("Press <Enter> to run the dice")
      dice = random.randrange(1,6)
      print("The dice is: ", str(dice))
      return dice


#-------------------------------------------------------------------------------------------
# The App starts here
#-------------------------------------------------------------------------------------------
while True:
    print(WelcomeMessage) 
    game_status = StartMenu()
    print(ThisIsTheStory)
    
    TheCharacter = CharacterMenu()
    print("Good luck! ")
    
    Game.SetTheActor(TheCharacter)
    CharacterRole = Game.GetTheCharacterRole()
    print(CharacterRole)
    CharacterAttributes = Game.GetTheCharacterAtributes()
    print(CharacterAttributes)
    
    RunChallenge = 1
    Game.SetCurrentChallenge(RunChallenge);
    Warnings = 0
    Game.SetNoOfWarnings(Warnings)
    Health = Game.GetActorHealth()
    ActiveMission = 1
    Dice = 1
    ChallengeResult = False
    while ActiveMission == 1:
        if RunChallenge == 1:
            print(MenuChallege_1_InfiltrateBase)
            user_choice = SelectionMenu(OptionsForChallenge_1)
            Dice = RollTheDice()
            ChallengeResult = Game.Challenge_1_EnterBase(user_choice, Dice) 
        elif RunChallenge == 2:
            print(MenuChallege_2_EvadeGuards)
            user_choice = SelectionMenu(OptionsForChallenge_2)
            Dice = RollTheDice()                
            ChallengeResult = Game.Challenge_2_EvadeGuards(user_choice, Dice)
        elif RunChallenge == 3:
            print(MenuChallege_3_FindVault)
            user_choice = SelectionMenu(OptionsForChallenge_3)
            Dice = RollTheDice()                
            ChallengeResult = Game.Challenge_3_FindVault(user_choice, Dice)
        elif RunChallenge == 4:
            print(MenuChallege_4_OpenVault)
            user_choice = SelectionMenu(OptionsForChallenge_4)
            Dice = RollTheDice()                
            ChallengeResult = Game.Challenge_4_OpenVault(user_choice, Dice)
        elif RunChallenge == 5:
            print(MenuChallege_5_EscapeBase)
            user_choice = SelectionMenu(OptionsForChallenge_5)
            Dice = RollTheDice()
            ChallengeResult = Game.Challenge_5_EscapeBase(user_choice, Dice)              
        else:
            print("This challenge is out of range.")
    
        Warnings = Game.UpdateWarningCount(ChallengeResult)
    
        RunChallenge += 1           
        Health = Game.GetActorHealth()
        print("Warnings: ", str(Warnings), " Health:", str(Health))
        if (RunChallenge > 5) or (Health <= 0) or (Warnings >= 3):
            ActiveMission = 0
    
        Game.SetCurrentChallenge(RunChallenge)
        PressEnterToContinuue()
    
    if (Health <= 0) or (Warnings >= 3):
        print("You failed this mission.")
    else:
        print("You succesfully completed the mission!")
      
    PressEnterToContinuue()
    
