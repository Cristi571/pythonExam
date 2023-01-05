

# Import built-in deps
from Models.Records import myRecords

class menuDelete :

    def __init__(self, query) :
        self.query = query
        if query : self.DeleteBy(query)
        return None



    def Content(self) :
        print(f"|------------------------------------------|\n"
            "|  What do you want to delete?             |\n"
            "|------------------------------------------|")
        return None



    def Options(self) :
        return {
            1 : 'Select All',
            2 : 'Select by ID',
            3 : 'Select by FName',
            4 : 'Select by LName',
            5 : 'Select by Age',
            6 : 'Select by City',
            7 : 'Back to main',
            0 : 'Exit App',
        }
    
    def Decisions(self) :
        try:
            while True :
                option = int(input('| Enter your choice: '))
                # print("|------------------------------------------|\n")
                if option == 0 : return("killMe")
                elif option == 1 : return("seeAll")
                elif option == 2 : return("findId")
                elif option == 3 : return("findFName")
                elif option == 4 : return("findLName")
                elif option == 5 : return("findAge")
                elif option == 6 : return("findCity")
                elif option == 7: return("**cancel")
                else:
                    print('Invalid! Please chose an option from the menu.')

        except Exception as e: 
            # print("An error occured : ")
            # print(e)
            print('Wrong input! Please enter a number.')
        return None
    
    def DeleteBy(self, query) :
        print(f"Deleting ..")
        print(f"query : {query.keys()}")
        print(f"data : {query.items()}")
        record = myRecords(None, None)
        for key, item in query.items() :
            record.DeleteAllBy(key, item)