#This is the App.py file. Created 2023.09.29
#take user input
#Explenation

def start_menu():
      while True:
            menu_start = input("Would you like to start the game: ")
            if menu_start == "y" or  menu_start == "Y" or  menu_start == "Yes":
                  return True  
            elif menu_start == "n" or  menu_start == "N" or  menu_start == "No": 
                  exit()
            else:
                  print("Please input a proper answer ex: Yes or No")


game_status = start_menu()


print(game_status)

print("Welcome to the choose your own adventure text based game.\n", ) 
print("An enemy nation has developed a bioweapon that is able to infect and wipe out an entire city in just a few days.\n" 
    "You are ordered to steal a sample of the bioweapon and the cure from the secret underground laboratory located in a military base.\n"
    "Only one person can go in to avoid suspicion. First is the spy, this character has been undercover as a scientist for many years.\n"
    "Second is the greatest thief, he has the best skill set and has the experience of many successful heists.\n"
    "There will be a 24-hour window where both the cure and weapon will be in the same vault.")


#story_dump = input("") 