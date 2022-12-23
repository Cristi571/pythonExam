
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




# Import all dependencies 
import csv
import string
import re
rootPath = "/Users/fr146574/Desktop/ESTIAM/E4_2022-2023/COURS/Python/Cours3/"




class File :
    def getAllDataFromCSV(fileName) :
        try :
            # Prepare the res data
            headTable = []
            bodyTable = []

            # Set default fileName
            if fileName == None :
                fileName = "pythonDB.csv"
            filePath = rootPath + fileName

            # Open the csv file
            with open(filePath, newline='') as file:
                # Read the data from csv file
                csvReader = csv.reader(file)
                try :
                    # Set the header of the DT
                    headTable = next(csvReader)
                    
                    # Set the content of the DT
                    for row in csvReader:
                        bodyTable.append(row)
                except :
                    print("The file contains no data")

            # Prepare the response
            return {
                "mess" : "ok", 
                "code" : 200, 
                "data" : {"head" : headTable, "body" : bodyTable}
            }
            
        except Exception as err: 
            # Display warning message
            print(f"An error occured : \n {err}")
            # Prepare the response
            return {
                "mess" : "bad",
                "code" : 500, 
                "data" : {"head" : [], "body" : []}
            }
    def putDataIntoCSV(fileName, data):
        print("<putDataIntoCSV> started ..")
        try :
            # Set default fileName
            if fileName == None :
                fileName = "pythonDB.csv"
            filePath = rootPath + fileName
            print(f"filePath : {filePath}")

            # Append all new data rows to the existing csv file data
            for row in data :
                with open(filePath, 'a') as file:
                    file.write(
                        "\n"+
                        str(row["id"])+", " +
                        str(row["lname"])+", " +
                        str(row["fname"])+", " +
                        str(row["age"])+", " +
                        str(row["city"])
                    )

        except Exception as err :
            # Display warning message
            print(f"Can't write data into csv file because an error occured : \n {err}")


class Data :
    # Get all data 
    def getAllRecords () :
        res = None
        try :
            query = File.getAllDataFromCSV(None)
            # Valid query result
            if query : 
                if query["mess"] == "ok" or query["code"] == 200 :
                    res = query
            # Invalid query result
            else :
                res = "No data records found."
        except Exception as e: 
            print("An error occured : ")
            print(e)
            res = None
        finally :
            return res



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
                0 : 'Exit',
            }
        

        # Option 1
        def AddNewRecord():
            try :
                print(" Adding new person ...")
                print(" Tip : To delimit combined names use one space (\" \"), rather than (\"-\")")
                print(" Tape (\"*#\") at any time to exit")
                print(" For empty facultative data (Age and City) just press \"Enter\"")
                print("...........................................")
                newID = 1
                res = Data.getAllRecords()
                if(res["mess"] == "ok" or res["code"] == 200) : 
                    if(len(res["data"]["body"]) > 0) :
                        lastID = res['data']['body'][-1][0]
                        newID = int(lastID)+1
                    else :
                        print("No data records")
                else :
                    print("Can't add new records right now, please try again later.")

                labels = ["First name : ", "Last name : ", "Age : ", "City : "]
                newRecord = [{"id" : newID, "fname" : "", "lname" : "", "age" : "", "city" : ""}]

                for label in labels :
                    # Set the First Name
                    taping = True
                    # Using a loop to let the user retry taping if invalid value
                    while(taping) :
                        userInput = input(label)
                        # Get the user raw input
                        if(userInput == "*#") :
                            print("Operation canceled..")
                            return 'canceled'
                        else :
                            try :
                                if(label == "First name : ") :
                                    if(re.match("^[a-zA-Z_ ]+$|\"*#\"", userInput)) :
                                        print("input matches")
                                        newRecord[0]["fname"] = string.capwords(userInput)
                                        taping = False
                                    else : 
                                        print("input doesn't match")
                                elif(label == 'Last name : ') :
                                    newRecord[0]["lname"] = string.capwords(userInput)
                                elif(label == 'Age : ') :
                                    newRecord[0]["age"] = int(userInput)
                                elif(label == 'City : ') :
                                    newRecord[0]["city"] = string.capwords(userInput)
                                
                            except Exception as e :
                                print("Invalid input, please retry.")
                                print(e)

                print("New record data preview :")
                print(newRecord)
                File.putDataIntoCSV(None, newRecord)

            except Exception as e :
                print(f"An error occured222 : \n {e}")


        # Option 2
        def DisplayAllRecords():
            try :
                # print('Handle option \'Option 2\'')
                res = Data.getAllRecords ()
                data = res["data"]

                # Prepare header data
                rowData = ""
                for cell in data["head"] :
                    rowData = f"{rowData}{cell} |"
                # Display header data
                print(" --------------------------------")
                print(f"| {rowData}")
                print(" --------------------------------")
                
                # Prepare and display body data
                for row in data["body"] :
                    rowData = ""
                    for cell in row :
                        rowData = f"{rowData}{cell} |"
                    print(f"| {rowData}")
                print(" --------------------------------")
                # print(res['mess'])

                # Display the menu2 for this section
                menu2 = True
                while(menu2) : 
                    print(" ==========================================")
                    print("|                   Menu 2                 |")
                    print(" ..........................................")
                    Menus.print_menu(Menus.Menu2.Options())
                    print(" ..........................................")
                    choise = Menus.Menu2.ManageUserInput()
                    if(choise == "back" or choise == "exit") :
                        menu2 = False
            except Exception as e :
                print(f"An error occured : \n {e}")

        def FindOneByID():
            try :
                print('Handle option \'Option 3\'')
            except Exception as e :
                print(f"An error occured : \n {e}")

        def FindOneByFName():
            try :
                print('Handle option \'Option 4\'')
            except Exception as e :
                print(f"An error occured : \n {e}")

        def FindOneByLName():
            try :
                print('Handle option \'Option 5\'')
            except Exception as e :
                print(f"An error occured : \n {e}")

        def UpdateOneByID(id):
            try :
                print('Handle option \'Option 6\'')
            except Exception as e :
                print(f"An error occured : \n {e}")
                
        def DeleteOneByID():
            try :
                print('Handle option \'Option 7\'')
            except Exception as e :
                print(f"An error occured : \n {e}")

        def DeleteAllRecords():
            try :
                print('Handle option \'Option 8\'')
            except Exception as e :
                print(f"An error occured : \n {e}")
        





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
                elif option == 2: Menus.MainMenu.DisplayAllRecords()
                elif option == 3: Menus.MainMenu.FindOneByID()
                elif option == 4: Menus.MainMenu.FindOneByFName()
                elif option == 5: Menus.MainMenu.FindOneByLName()
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
                0 : 'Exit',
            }
        
        def ManageUserInput() :
            try:
                option = int(input('Enter your choice: '))
                print(" ------------------------------------------")
                if option == 0: 
                    App.kill()
                    return 'exit'
                elif option == 1: Menus.MainMenu.AddNewRecord()
                elif option == 2: Menus.MainMenu.FindOneByID()
                elif option == 3: Menus.MainMenu.FindOneByFName()
                elif option == 4: Menus.MainMenu.FindOneByLName()
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








    













class App :
    runState = True

    # Used to start the app
    def run() :
        # Initiate an instance of MainMenu
        mainMenu = Menus.MainMenu
        # Run the app untill exit
        while(App.runState == True) :

            print(" ==========================================")
            print("|                    Menu                  |")
            print(" ..........................................")
            Menus.print_menu(mainMenu.Options())
            print(" ..........................................")
            mainMenu.ManageUserInput() 
            print(" ==========================================")
        return None
    
    # Used to exit the app
    def kill() :
        print('Bye, return back soon.')
        App.runState = False
        return None



App.run()

        
