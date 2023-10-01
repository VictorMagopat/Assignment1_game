#This is the App.py file. Created 2023.09.29

# This file implements the interaction with the user.
# Sends the user's input to the game engine.

#import Role1
#import Role2
import Game


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

ThisIsChallege_1 = """
      Challenge 1___________________________
      <1> Sneak in on an army vehicle
      <2> Climb building and enter the vents
      <3> Main entrance"""

ThisIsChallege_2 = """
      Challenge 2___________________________
      <1> Bluff past 
      <2> Sneak past
      <3> Suprise attack"""

ThisIsChallege_3 = """
      Challenge 3___________________________
      <1> Ask the head scientist for location
      <2> Intimidate head scientist"""

ThisIsChallege_4 = """
      Challenge 4___________________________
      <1> Unlock vault"""

ThisIsChallege_5 = """
      Challenge 5___________________________
      <1> Sneak out
      <2> Bluff past"""

# the user is choosing to play the game or exit
def StartMenu():
      while True:
            menu_start = input("Would you like to start the game: ")
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



def PressEnterToContinuue():
      WaitHere = input("Press <Enter> to continue")


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
      while ActiveMission == 1:
            if RunChallenge == 1:
                print(ThisIsChallege_1)
                user_choice = SelectionMenu(3)
                Game.Challenge_1(user_choice) 
            elif RunChallenge == 2:
                print(ThisIsChallege_2)
                user_choice = SelectionMenu(3)
                Game.Challenge_2(user_choice)
            elif RunChallenge == 3:
                print(ThisIsChallege_3)
                user_choice = SelectionMenu(2)
                Game.Challenge_3(user_choice)
            elif RunChallenge == 4:
                print(ThisIsChallege_4)
                user_choice = SelectionMenu(2)
                Game.Challenge_4(user_choice)
            elif RunChallenge == 5:
                print(ThisIsChallege_5)
                user_choice = SelectionMenu(2)
                Game.Challenge_5(user_choice)                
            else:
                print("This challenge is out of range.")

            RunChallenge += 1                        
            Warnings = Game.GetNoOfWarnings()
            Health = Game.GetActorHealth()
            print("Warnings: ", str(Warnings), " Health:", str(Health))

            if (RunChallenge > 5) or (Health <= 0) or (Warnings >= 3):
                ActiveMission = 0

            Game.SetCurrentChallenge(RunChallenge);
#            PressEnterToContinuue()
      
      if (Health <= 0) or (Warnings >= 3):
          print("You failed this mission.")
      else:
          print("You succesfully completed the mission!")
      PressEnterToContinuue()

