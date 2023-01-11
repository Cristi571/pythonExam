

from Models.MenuMain import myMainMenu
from Models.Records import myRecords
from Models.MenuAdd import menuAddNew
from Models.MenuSeeAll import menuSeeAll

class myMenuTools :

    # Menu constructor
    def __init__(self, prev, curr):
        self.prevMenu = prev
        self.currMenu = curr

    def Display(self):
        # Initialize the menu
        menu = myMainMenu
        if self.currMenu == "main" :
            menu = myMainMenu
        elif self.currMenu == "addNew" :
            menu = menuAddNew
        elif self.currMenu == "seeAll" :
            menu = menuSeeAll
            

        try :
            data = menu.Content()
            # Create the menu interface to display
            options = menu.Options()
            print(self.MenuInterface(options))

            
            # Get the user input
            decision = menu.Decisions()
            print("#==========================================#")


            if self.currMenu == "addNew" and data :
                if decision == "submit" :
                    res = menu.SubmitData(data)
                    if res == 'ok' :
                        self.currMenu = 'main'
                        data, options, decision = None

            return decision
        except Exception as err :
            print("Can't display menu. \n"
                "Please restart the app.\n"
                 "  Source : myMenuTools->Display() \n"
                f"  Error  : {err}")
            
            return None
            


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
                "|                    Menu                  |\n"
                "#..........................................#\n"
                f"{menuBody[:-1]}\n"
                "#------------------------------------------#")
