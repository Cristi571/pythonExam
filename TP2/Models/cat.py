

# Import built-in deps
import random
from Models.animal import Animal


class Cat(Animal) :
    # Chat constructor
    def __init__(self, name, age):
        try :
            # Call the parent class constructor (Animal)
            # to set the name argument for the animal
            super().__init__(name, age)
            self.age = age
        except Exception as err :
            print("Source : Cat->init() \n"
                f"Error : {err}")

    def cri(self) :
        # Randomize the cry to make it more dynamic and interactive
        sound = ""
        for x in range(0, random.randint(1, 3)) :
            sound = sound + "Miaou! "
        print(sound)

