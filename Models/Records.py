

# Import built-in deps
import string
import re
import os
# from Models.Data import myData
from Models.Files import myFile

"""
Determines csv records managment methods
Essential CRUD Records
"""
class myRecords :
    # Record constructor
    def __init__(self, root, file):
        if not root :
            self.root = os.path.dirname(os.path.abspath("__file__")) + "\\"
        else :
            self.root = root

        if not file :
            self.file = "pythonDB.csv"
        else :
            self.file = file

    """
    Append new row(s) to existing data in the given csv file
    Tries to automatically determine the record ID
    """
    def AddNewRecord(self, data):
        # print(f"data : {data}")
        if not data :
            # print("Nothing to add.")
            return "NoData"

        try :
            try:
                file = myFile(None, None)
                res = file.getAllDataFromCSV()
                
                if(res["mess"] == "ok" or res["code"] == 200) : 
                    if(len(res["data"]["body"]) > 0) :
                        lastID = res['data']['body'][-1][0]
                        data[0]["id"] = int(lastID)+1
                    else :
                        print("No data records")
            except :
                data[0]["id"] = 1

            print(f"Data preview : {data}")
            res = file.putDataIntoCSV(data)
            return res
        except Exception as err :
            # Display warning message
            print("/!\\   Warning ! \n"
                "An error occured at \n"
                "  Source : Records->AddNewRecord() \n"
                f"  Error  : {err}")
            return 'bad'


    """"""
    def getAllRecords(self):
        try :
            # print('Handle option \'Option 2\'')
            file = myFile(None, None)
            res = file.getAllDataFromCSV()
            return res["data"]

        except Exception as e :
            print(f"Can't display data because an error occured : \n {e}")



    """"""
    def FindOneByID(self, id):
        try :
            print('Handle option \'Option 3\'')
            data = self.getAllRecords()
            print(f"data : {data}")

            # Prepare header data
            dataHeader = ""
            for cell in data["head"] :
                dataHeader = f"{dataHeader}{cell} |"
            # Display header data
            dataHeader = f"| {dataHeader}"
            # print("#------------------------------------------#")
            # print(f"| {dataHeader}")
            # print("#------------------------------------------#")
            

            # Prepare body data
            dataBody = ""
            count = 0
            for row in data["body"] :
                rowData = ""
                print(f"id {row[0]}")
                if int(row[0]) == int(id) :
                    count += 1
                    for cell in row :
                        rowData = f"{rowData}{cell} |"
                    print()
                    dataBody = f"{dataBody} \n| {rowData}"

            print("#------------------------------------------#")
            if count > 0 :
                print(f"| {count} result(s) found :                      |")
                print("#------------------------------------------#")
                print(dataHeader)
                print("#------------------------------------------#")
                print(dataBody[2:])
            else :
                print("No results found.")
            print("#------------------------------------------#")

            
        except Exception as e :
            print(f"An error occured : \n {e}")
    

    """"""
    def FindOneByFName():
        try :
            print('Handle option \'Option 4\'')
        except Exception as e :
            print(f"An error occured : \n {e}")


    """"""
    def FindOneByLName():
        try :
            print('Handle option \'Option 5\'')
        except Exception as e :
            print(f"An error occured : \n {e}")


    """"""
    def UpdateOneByID(id):
        try :
            print('Handle option \'Option 6\'')
        except Exception as e :
            print(f"An error occured : \n {e}")


    """"""
    def DeleteOneByID():
        try :
            print('Handle option \'Option 7\'')
        except Exception as e :
            print(f"An error occured : \n {e}")


    """"""
    def DeleteAllRecords():
        try :
            print('Handle option \'Option 8\'')
        except Exception as e :
            print(f"An error occured : \n {e}")
        