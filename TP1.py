
# ==============================================================================

# TP 1 :

# Ecrivez un programme qui prend en entrée un fichier csv 
# contenant des informations sur plusieurs personnes, 
# chacune sur une ligne différente, sous la forme "nom, prénom, âge, ville". 
# Le programme doit lire ce fichier et créer un dictionnaire 
# pour chaque personne, avec les informations du fichier en tant que 
# valeurs associées aux clés "nom", "prenom", "age" et "ville".

# Le programme doit ensuite afficher un menu permettant à l'utilisateur de :
#  - Afficher la liste de toutes les personnes enregistrées, 
#    sous la forme "nom prénom, âge ans, ville"
#  - Ajouter une nouvelle personne en saisissant les informations au clavier
#  - Modifier les informations d'une personne en saisissant son nom 
#    et en modifiant les informations souhaitées
#  - Supprimer une personne en saisissant son nom

# Voici un exemple de ce à quoi ressemble le format csv :
# Doe, John, 30, Paris
# Smith, Mary, 25, New York

# ==============================================================================




# Import built-in dependencies 
import string
import re
# Import local dependencies and classes
from Models.App import App
from Models.Files import File
# from Models.Data import Data

# rootPath = "/Users/fr146574/Desktop/ESTIAM/E4_2022-2023/COURS/Python/Cours3/"



class Menus :
    currentMenu = "main"

    def print_menu(menu):
        for key in menu.keys():
            print (f"{key} : {menu[key]}" )

    # -------------- Menu 2 --------------
    class MainMenu :
        # Define the main menu options to display
        def Options() :
            return {
                # Create
                1 : 'Add a new person',
                # Read
                2 : 'See all',
                3 : 'Find a person by ID',
                4 : 'Find a person by FName',
                5 : 'Find a person by LName',
                # Update
                6 : 'Update a person data',
                # Delete
                7 : 'Delete a person data',
                # Other options
                0 : 'Exit App',
            }





        def Decisions() :
            return None
        
        def ManageUserInput() :
            try:
                option = None
                option = int(input('Enter your choice: '))
                print(" ------------------------------------------")
                print("")
                if option == 0: 
                    App.kill()
                    return None
                elif option == 1: Menus.MainMenu.AddNewRecord()
                elif option == 2: Menus.MainMenu.getAllRecords()
                elif option == 3: Menus.MainMenu.FindAllByID()
                elif option == 4: Menus.MainMenu.FindAllByFName()
                elif option == 5: Menus.MainMenu.FindAllByLName()
                elif option == 6: Menus.MainMenu.UpdateOneByID()
                elif option == 7: Menus.MainMenu.DeleteOneByID()
                else:
                    print('Invalid option. Please enter a number from the menu.')
            except Exception as e: 
                print("An error occured11 : ")
                print(e)
                print('Wrong input! Please enter a number.')

            return None




    # -------------- Menu 2 --------------
    class Menu2 :
        def Options() :
            return {
                # Create
                1 : 'Add a new person',
                # Read
                2 : 'Select a person by ID',
                3 : 'Select a person by FName',
                4 : 'Select a person by LName',
                # Update
                5 : 'Update a person data',
                # Delete
                6 : 'Delete a person data',
                7 : 'Delete all data',
                # Other options
                8 : 'Back',
                0 : 'Exit App',
            }
        
        def ManageUserInput() :
            try:
                option = int(input('Enter your choice: '))
                print(" ------------------------------------------")
                if option == 0: 
                    App.kill()
                    return 'exit'
                elif option == 1: Menus.MainMenu.AddNewRecord()
                elif option == 2: Menus.MainMenu.FindAllByID()
                elif option == 3: Menus.MainMenu.FindAllByFName()
                elif option == 4: Menus.MainMenu.FindAllByLName()
                elif option == 5: Menus.MainMenu.UpdateOneByID()
                elif option == 6: Menus.MainMenu.DeleteOneByID()
                elif option == 7: Menus.MainMenu.DeleteAllRecords()
                elif option == 8: return 'back'
                else:
                    print('Invalid option. Please enter a number from the menu.')
            except Exception as e: 
                print("An error occured : ")
                print(e)
                print('Wrong input! Please enter a number.')

            return None
        
        def defaul() :
            return None








    













# class App :
#     runState = True

#     # Used to start the app
#     def run() :
#         # Initiate an instance of MainMenu
#         mainMenu = Menus.MainMenu
#         # Run the app untill exit
#         while(App.runState == True) :

#             print(" ==========================================")
#             print("|                    Menu                  |")
#             print(" ..........................................")
#             Menus.print_menu(mainMenu.Options())
#             print(" ..........................................")
#             mainMenu.ManageUserInput() 
#             print(" ==========================================")
#         return None
    
#     # Used to exit the app
#     def kill() :
#         print('Bye, return back soon.')
#         App.runState = False
#         return None



# App.run()

        
