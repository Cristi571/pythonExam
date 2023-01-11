

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
            3 : 'Find by ID',
            4 : 'Find by FName',
            5 : 'Find by LName',
            6 : 'Find by Age',
            7 : 'Find by City',
            # Update
            8 : 'Update data',
            # Delete
            9 : 'Delete data',
            # Other options
            0 : 'Exit App',
        }
    

    def Decisions() :
        try:
            while True :
                option = int(input('| Enter your choice: '))
                if option == 0 : return "killMe"
                elif option == "**": return "**cancel"
                elif option == 1 : return("addNew")
                elif option == 2 : return("seeAll")
                elif option == 3 : return("findId")
                elif option == 4 : return("findFName")
                elif option == 5 : return("findLName")
                elif option == 6 : return("findAge")
                elif option == 7 : return("findCity")
                elif option == 8 : return("update")
                elif option == 9 : return("delete")
                else:
                    print('Invalid! Please chose an option from the menu.')

        except Exception as e: 
            print('Wrong input! Please enter a number.')

        return None