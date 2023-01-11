

from Models.ferme import Ferme
from Models.dog import Dog
from Models.cat import Cat

class Main : 

    maFerme = Ferme()

    runState = True
    while runState == True :
        print("\n Menu : \n"
            " 1 : See all animals \n"
            " 2 : Add a dog \n"
            " 3 : Add a cat \n"
            " 4 : Kill an animal \n"
            " 0 : Exit app"
            )
        try :
            choice = int(input("Select an option : "))
            print("\n")
            ferme = Ferme
            newAnimal = None

            if(choice == 0) :
                print("Bye, come back soon.")
                runState = False
            elif(choice == 1) :
                ferme.show("all")

            elif(choice == 2) :
                while True :
                    print("Adding a dog ..")
                    name = str(input("Name : "))
                    age = int(input("Age : "))
                    newAnimal = Dog(name, age)
                    if(ferme.add(newAnimal) == 'ok'):
                        if(ferme.crier() != 'ok') :
                            print("Trop fatigué pour crier..")
                        break

            elif(choice == 3) :
                while True :
                    print("Adding a cat ..")
                    name = str(input("Name : "))
                    age = int(input("Age : "))
                    newAnimal = Cat(name, age)
                    if(ferme.add(newAnimal) == 'ok'):
                        if(ferme.crier() != 'ok') :
                            print("Trop fatigué pour crier..")
                        break

            elif(choice == 4) :
                while True :
                    print("Killing an animal ..")
                    print("Type ** to exit.")
                    entry = str(input("Name : "))
                    if entry == "**" :
                        choice = None
                        break
                    res = ferme.kill(entry)
                    if (res == "ok") :
                        break
                    print("\n")
                            

            else :
                print("Invalid. Please retry.")

        except Exception as err :
            print("Invalid. Please enter a number.")
            print("Source : Main() \n"
                f"Error : {err}")
        
