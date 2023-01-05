

# Import built-in deps

from Models.Records import myRecords

class menuSeeAll :

    def Content() :
        record = myRecords(None, None)
        data = record.getAllRecords()

        # Prepare header data
        rowData = ""
        for cell in data["head"] :
            rowData = f"{rowData}{cell} |"
        # Display header data
        print("#------------------------------------------#")
        print(f"| {rowData}")
        print("#------------------------------------------#")
        
        # Prepare and display body data
        for row in data["body"] :
            rowData = ""
            for cell in row :
                rowData = f"{rowData}{cell} |"
            print(f"| {rowData}")
        print("#------------------------------------------#")

        return None

    def Options() :
        return {
            1 : 'Select by ID',
            2 : 'Select by First Name',
            3 : 'Select by Last Name',
            4 : 'Delete all the data',
            5 : 'Back to main',
            0 : 'Exit App',
        }
    
    def Decisions() :
        try:
            while True :
                option = int(input('| Enter your choice: '))
                print("|------------------------------------------|\n")
                if option == 0: return "killMe"
                elif option == 1 : return("findId")
                elif option == 2 : return("findFName")
                elif option == 3 : return("findLName")
                elif option == 4 : return({
                        "action" : "delete",
                        "query" : "all"})
                elif option == 5 : return("**cancel")
                else:
                    print('Invalid! Please enter an option from the menu.')

        except Exception as e: 
            print("An error occured : ")
            print(e)
            print('Wrong input! Please enter a number.')

