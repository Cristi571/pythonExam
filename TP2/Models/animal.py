

# Import built-in deps


class Animal :
    # Animal constructor
    def __init__(self, name : str, age : int) :
        try :
            self.name = name 
            self.age = age 
        except Exception as err :
            print("Source : Animal->init() \n"
                f"Error : {err}")
        
    # Initialize the animal cry
    # This means every animal can cry but each of them have it's own cry
    def cri(self) :
        pass