

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
        else : self.root = root

        if not file :
            self.file = "pythonDB.csv"
        else : self.file = file

    """
    Append new row(s) to existing data in the given csv file
    Tries to automatically determine the record ID
    """
    def AddNewRecord(self, data):
        if not data :
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
            file = myFile(None, None)
            res = file.getAllDataFromCSV()
            return res["data"]

        except Exception as e :
            print(f"Can't display data because an error occured : \n {e}")



    """"""
    def FindAllBy(self, method, query):
        try :
            data = self.getAllRecords()

            # Prepare header data
            dataHeader = ""
            for cell in data["head"] :
                dataHeader = f"{dataHeader}{cell} |"
            # Display header data
            dataHeader = f"| {dataHeader}"

            # Prepare body data
            dataBody = ""
            count = 0
            searchCol = -1
            if method == "ID" :
                searchCol = 0
            elif method == "LName" :
                searchCol = 1
            elif method == "FName" : 
                searchCol = 2
            elif method == "Age" : 
                searchCol = 3
            elif method == "City" : 
                searchCol = 4
            
            if searchCol >= 0 :
                for row in data["body"] :
                    # Skip rows that do not respect data format
                    if len(row) != 4 :
                        continue

                    rowData = ""
                    if str(row[searchCol]).strip().lower() == str(query).strip().lower() :
                        count += 1
                        for cell in row :
                            rowData = f"{rowData}{cell} |"
                        dataBody = f"{dataBody} \n| {rowData}"
            else :
                print(f"Something went wrong, please retry.")
                

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
    def UpdateByID(self, id):
        try :
            print('Update by ID ..')
        except Exception as e :
            print(f"An error occured : \n {e}")


    """"""
    def DeleteAllBy(self, method, query):
        try :
            data = self.getAllRecords()
            
            # Set the filter criteria
            searchCol = -1
            if method == "ID" :
                searchCol = 0
            elif method == "LName" :
                searchCol = 1
            elif method == "FName" : 
                searchCol = 2
            elif method == "Age" : 
                searchCol = 3
            elif method == "City" : 
                searchCol = 4

            newData = []
            # Add header data
            newData.append(data['head'])
            
            # Prepare body data
            count = 0
            dataBody = []
            if searchCol >= 0 :
                for row in data["body"] :
                    # Except/Exclude elements to delete
                    if str(row[searchCol]).strip().lower() != str(query).strip().lower() :
                        count += 1
                        newData.append(row)
            else :
                print(f"Something went wrong, please retry.")

            file = myFile(None, None)
            file.ReWriteDataIntoCSV(newData)

        except Exception as e :
            print(f"An error occured : \n {e}")


    """"""
    def DeleteAllRecords(self):
        try :
            file = myFile(None, None)
            newData = [['ID', ' LName', ' FName', ' Age', ' City']]
            file.ReWriteDataIntoCSV(newData)
        except Exception as e :
            print(f"An error occured : \n {e}")