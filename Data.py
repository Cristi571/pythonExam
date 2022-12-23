


from Files import Files as File

"""
The Data class regroups methods to manpulate and validate data
"""
class Data :
    """
    Checks the response after reading csv file
    Returns an interpreted response after response data validation
    If reading csv file sends positive response 
    the raw data is returne or an informative message
    None is returned in case of unexpected exception
    """
    def getAllRecords () :
        res = None
        try :
            query = File.getAllDataFromCSV(None)
            # Valid query result
            if query : 
                if query["mess"] == "ok" or query["code"] == 200 :
                    res = query
            # Invalid query result
            else :
                res = "No data records found."
        except Exception as e: 
            print("An error occured : ")
            print(e)
            res = None
        finally :
            return res