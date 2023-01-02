

import csv
import os

class myFile :
    # File constructor
    def __init__(self, root, file):
        if not root  :
            self.root = os.path.dirname(os.path.abspath("__file__")) + "\\"
        else :
            self.root = root

        if not file :
            self.file = "pythonDB.csv"
        else :
            self.file = file



    """
        Reads a given csv file and return a response of type Dict
        The response contains :
        @mess [String | "ok", "bad"]
        @code [Int | 200 : success, 400 : empty, 404 : not found, 500 : exception]
        @data [Dict | head : table header, body : table body]
            @@head [Array | strings]
            @@body [Array | arrays of string]
    """
    def getAllDataFromCSV(self) :
        # Access the global variables
        global csv

        try :
            # Prepare the res data
            headTable = []
            bodyTable = []
            filePath = self.root + self.file
            
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
            print("/!\\   Warning ! \n"
                "An error occured at \n"
                "  Source : File->getAllDataFromCSV() \n"
                f"  Error  : {err}")
            # Prepare the response
            return {
                "mess" : "bad",
                "code" : 500, 
                "data" : {"head" : [], "body" : []}
            }


    def putDataIntoCSV(self, data):
        # Access the rootPath variable
        global csv
        # print("<putDataIntoCSV> started ..")
        try :
            filePath = self.root + self.file
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
            return "ok"

        except Exception as err :
            # Display warning message
            print(f"Can't write data into csv file because an error occured : \n {err}")
            return 'bad'