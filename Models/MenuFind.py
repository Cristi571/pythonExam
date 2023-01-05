

# Import built-in deps
import re
from Models.Records import myRecords

class menuFind :
    def __init__(self, method, query):
        if method :
            self.method = method
        else :
            self.method = "ID"
        # Used to design the selection
        self.query = query
        return None



    def Content(self) :
        print("#------------------------------------------#\n"
            " Tips : \n"
            "* Type ** at any time to exit\n"
            "#------------------------------------------#")
        print(f"method : {self.method}")

        userInput = None
        while True :
            if self.method == "ID" :
                userInput = input("Enter the ID : ")
                if userInput.isdigit() and int(userInput) >= 0 :
                    record = myRecords(None, None)
                    res = record.FindAllBy("ID", userInput)
                    self.query = {"ID" : userInput}
                    print(f"res : {res}")
                    break
                else :
                    print("Invalid. IDs can contain only digits")
            elif self.method == "FName" :
                userInput = input("Enter the First Name : ")
                if re.match("^[a-zA-Z_ àâçéèêëîïôûùüÿñæœ]+$", userInput) :
                    record = myRecords(None, None)
                    res = record.FindAllBy("FName", userInput)
                    self.query = {"FName" : userInput}
                    print(f"res : {res}")
                    break
                else :
                    print("Invalid! Only alphabetical, spaces and \"**\" are allowed.")
            elif self.method == "LName" :
                userInput = input("Enter the Last Name : ")
                if re.match("^[a-zA-Z_ àâçéèêëîïôûùüÿñæœ]+$", userInput) :
                    record = myRecords(None, None)
                    res = record.FindAllBy("LName", userInput)
                    self.query = {"LName" : userInput}
                    break
                else :
                    print("Invalid! Only alphabetical, spaces and \"**\" are allowed.")

        print(f"userInput : {userInput}")

        if(userInput == "**") :
            return '**cancel'

        return userInput


    def Options(self) :
        return {
            1 : 'Delete',
            2 : 'Back to main',
            0 : 'Exit App',
        }
    
    def Decisions(self) :
        while True :
            try:
                print("|------------------------------------------|")
                option = int(input('| Enter your choice: '))
                print("|------------------------------------------|")
                if option == 0: return "killMe"
                elif option == 1 : 
                    return({
                        "action" : "delete",
                        "query" : self.query})
                elif option == 2 : return("**cancel")
                else:
                    print('Invalid! Please enter an option from the menu.')

            except Exception as e: 
                print("An error occured : ")
                print(e)
                print('Wrong input! Please enter a number.')
