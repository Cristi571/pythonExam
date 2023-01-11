

# Import built-in deps
import string
import re
from Models.Records import myRecords

class menuAddNew :
    def Content() :
        print(" Adding new person ...")
        print("#------------------------------------------#")
        print(" Tips : \n"
            "* To delimit combined names \n"
            "  use one space (\" \"), rather than (\"-\")")
        print("* Type ** at any time to exit")
        print("* For empty facultative data (Age and City)\n"
            "  just press \"Enter\"")
        print("#------------------------------------------#")

        labels = ["First name : ", "Last name : ", "Age : ", "City : "]
        newRecord = [
            {"id" : 0, "fname" : "", "lname" : "", "age" : "", "city" : ""}
        ]
 
        for label in labels :
            # Using a loop to let user retry taping if invalid value
            while(True) :
                # Get the user raw input
                userInput = input(label)
                
                # Check if user wants to cancel
                if(userInput == "**") :
                    print("#------------------------------------------#\n"
                    "  Operation canceled..")
                    return '**cancel'

                # Trying to get input data and format it if needed
                try :
                    # Set the First Name
                    if(label == "First name : ") :
                        if userInput == "":
                            print("Invalid! First name can not be empty.")
                        # Use RegEx to validate inputs
                        elif(re.match("^[a-zA-Z_ àâçéèêëîïôûùüÿñæœ]+$", userInput)) :
                            newRecord[0]["fname"] = string.capwords(userInput)
                            break # Valid input, pass to next
                        else : 
                            print("Invalid! Only alphabetical, spaces and \"**\" are allowed.")
                    
                    # Set the Last Name
                    elif(label == 'Last name : ') :
                        if userInput == "":
                            print("Invalid! Last name can not be empty.")
                        # Use RegEx to validate inputs
                        elif(re.match("^[a-zA-Z_ àâçéèêëîïôûùüÿñæœ]+$", userInput)) :
                            newRecord[0]["lname"] = string.capwords(userInput)
                            break # Valid input, pass to next
                        else : 
                            print("Invalid! Only alphabetical, spaces and \"**\" are allowed.")

                    # Set the Age
                    elif(label == 'Age : ') :
                        if userInput == "" :
                            newRecord[0]["age"] = "N/A"
                            break # Valid input, pass to next
                        # Check if the input is a digit
                        elif userInput.isdigit() :
                            # Limit age variation between 0(newborn) and 150()
                            if 0 <= int(userInput) <= 150 :
                                newRecord[0]["age"] = userInput
                                break # Valid input, pass to next
                            else :
                                print("[- Invalid age : allowed in range of 0 to 150 -]")
                        else :
                            print("Invalid! Only int numbers are allowed.")
            
                    # Set the City
                    elif(label == 'City : ') :
                        if userInput == "" :
                            newRecord[0]["city"] = "N/A"
                            break # Valid input, pass to next
                        # Use RegEx to validate inputs
                        elif(re.match("^[a-zA-Z_ àâçéèêëîïôûùüÿñæœ]+$", userInput)) :
                            # Capitalize city name
                            newRecord[0]["city"] = string.capwords(userInput)
                            break # Valid input, pass to next
                        else : 
                            print("Invalid! Only alphabetical, spaces and \"**\" are allowed.")

                # Manage exceptions
                except Exception as e :
                    print("Invalid input, please retry.")
                    print(e)

        return newRecord



    def Options() :
        return {
            1 : 'Submit',
            2 : 'Input again',
            3 : 'Back to main',
            0 : 'Exit App',
        }
    
    def Decisions() :
        while True :
            try:
                print("|------------------------------------------|")
                option = int(input('| Enter your choice: '))
                print("|------------------------------------------|")
                if option == 0: return "killMe"
                elif option == 1 : return("submit")
                # if self.currMenu == "addNew" and data :
                #     if decision == "submit" :
                elif option == 2 : return("retry")
                elif option == 3 : return("**cancel")
                else:
                    print('Invalid! Please enter an option from the menu.')

            except Exception as e: 
                print('Wrong input! Please enter a number.')
                print("An error occured : ")
                print(e)
    

    def SubmitData(data) :
        try :
            record = myRecords(None, None)
            return record.AddNewRecord(data)

        except Exception as err :
            print("An error occured : \n"
                 "  Source : MenuAdd->SubmitData() \n"
                f"  Error  : {err}")
            return 'bad'

