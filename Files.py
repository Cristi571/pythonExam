



class Files :
    import csv
    rootPath = "/Users/fr146574/Desktop/ESTIAM/E4_2022-2023/COURS/Python/Cours3/"

    def __init__(self, rootPath):
      self.rootPath=rootPath


    """
        Reads a given csv file and return a response of type Dict
        The response contains :
        @mess [String | "ok", "bad"]
        @code [Int | 200 : success, 400 : empty, 404 : not found, 500 : exception]
        @data [Dict | head : table header, body : table body]
            @@head [Array | strings]
            @@body [Array | arrays of string]
    """
    def getAllDataFromCSV(fileName) :
        # Access the global variables
        global rootPath
        global csv

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
        # Access the rootPath variable
        global rootPath
        global csv
        # print("<putDataIntoCSV> started ..")
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