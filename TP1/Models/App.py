

# Import built-in deps
import os

from Models.MenuMain import myMainMenu
from Models.MenuAdd import menuAddNew
from Models.MenuSeeAll import menuSeeAll
from Models.MenuFind import menuFind
from Models.MenuUpdate import menuUpdate
from Models.MenuDelete import menuDelete


class myApp :
    # Application constructor
    def __init__(self, runState, infoMess, prev, curr):
        self.runState = runState
        self.infoMess = infoMess
        self.prevMenu = prev if prev else "main"

        if curr == "main" :
            self.currMenu = myMainMenu
        elif curr == "addNew" :
            self.currMenu = menuAddNew
        elif curr == "seeAll" :
            self.currMenu = menuSeeAll
        elif curr == "find" :
            self.currMenu = menuFind(None, None)
        elif curr == "update" :
            self.currMenu = menuUpdate
        elif curr == "delete" :
            self.currMenu = menuDelete
        else :
            self.currMenu = myMainMenu

        
        

    # Used to start the app
    def run(self) :
        # print("[- App starting.. -]")
        wlkmHeader = """ __________________________________________ 
|                                          |
|                 Hello !                  |
|       Enjoy your time with myApp.        |
|__________________________________________|\n"""

        # Run the app untill exit by user choice
        # or unexpected exception
        while(self.runState == True) :
            try :
                # Use clear() to clear the console content automatically
                # for better user experience
                clear = lambda: os.system('cls')
                # clear()
                if self.infoMess : 
                    print(" ------------------------------------------")
                    print(self.infoMess)
                    print(" ------------------------------------------")
                    self.infoMess = None
                if self.currMenu == myMainMenu:
                    print(wlkmHeader)


                data = self.currMenu.Content()
                if data == "**cancel" :
                    data = None

                # Create and print the menu interface to display
                options = self.currMenu.Options()
                print(self.MenuInterface(options))


                # Get the user input
                decision = self.currMenu.Decisions()

                if decision == "killMe" :
                    self.prevMenu, self.currMenu, decision = None, None, None
                    self.kill()
                elif decision == "**cancel" :
                    decision = None
                    self.currMenu = myMainMenu
                    self.infoMess = "    Operation canceled."
                elif decision == "addNew" :
                    self.prevMenu = myMainMenu
                    self.currMenu = menuAddNew
                elif decision == "seeAll" :
                    self.prevMenu = myMainMenu
                    self.currMenu = menuSeeAll
                elif decision == "findId" :
                    self.prevMenu = myMainMenu
                    self.currMenu = menuFind("ID", None)
                elif decision == "findFName" :
                    self.prevMenu = myMainMenu
                    self.currMenu = menuFind("FName", None)
                elif decision == "findLName" :
                    self.prevMenu = myMainMenu
                    self.currMenu = menuFind("LName", None)
                elif decision == "findAge" :
                    self.prevMenu = myMainMenu
                    self.currMenu = menuFind("Age", None)
                elif decision == "findCity" :
                    self.prevMenu = myMainMenu
                    self.currMenu = menuFind("City", None)
                elif decision == "update" :
                    self.prevMenu = myMainMenu
                    self.currMenu = menuUpdate
                elif type(decision) == dict :
                    if decision['action'] == "delete" :
                        self.prevMenu = myMainMenu
                        self.currMenu = menuDelete(decision["query"])
                elif decision == "submit" :
                        res = self.currMenu.SubmitData(data)
                        self.currMenu = myMainMenu
                        data, options, decision = None, None, None
                        if res == 'ok' : 
                            self.infoMess = "  Data added successfully."
                        elif res == 'bad' : self.infoMess = "  Failed to add data."
                        elif res == 'NoData' : self.infoMess = "  Nothing to add."

                print("#==========================================#")                    


            except Exception as err:
                print("#- App crashed. Please restart. -#\n"
                    "  Source : App->run() \n"
                    f"  Error  : {err}")
                self.kill()

            

    # Prepare the menu interface to display
    def MenuInterface(self, options) :
        menuBody = ""
        for key, val in options.items():
            spaces = ""
            for i in range(40 - len(val) - len(str(key)) - 2) :
                spaces = spaces + " "
            if len(str(key)) == 1 :
                # Prepare the structure of each line
                menuBody = menuBody + (f"| {key} : {val}{spaces}|\n")
            elif len(str(key)) >= 2 :
                # Shift to left by 1 space if the key has 2 or more digits
                menuBody = menuBody + (f"|{key} : {val}{spaces} |\n")

        # Return menu interface
        return ("#==========================================#\n"
                "|                   Menu                   |\n"
                "#..........................................#\n"
                f"{menuBody[:-1]}\n"
                "#------------------------------------------#")
    
    
    
    # Used to exit the app
    def kill(self) :
        clear = lambda: os.system('cls')
        # clear()
        print(  " __________________________________________\n"
                "|                                          |\n"
                "|           Bye, come back soon.           |\n"
                "|__________________________________________|\n")
        self.runState = False
        return None