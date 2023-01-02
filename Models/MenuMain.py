

class myMainMenu :
    def Content() :
        return None


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
        try:
            while True :
                option = int(input('| Enter your choice: '))
                # print("|------------------------------------------|\n")
                if option == 0 : return "killMe"
                elif option == "**": return "**cancel"
                elif option == 1 : return("addNew")
                elif option == 2 : return("seeAll")
                elif option == 3 : return("findId")
                elif option == 4 : return("findFName")
                elif option == 5 : return("findLName")
                elif option == 6 : return("update")
                elif option == 7 : return("delete")
                else:
                    print('Invalid! Please chose an option from the menu.')

        except Exception as e: 
            # print("An error occured : ")
            # print(e)
            print('Wrong input! Please enter a number.')

        return None