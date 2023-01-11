

from Models.animal import Animal

class Ferme :

    animals = []

    def show(criteria) :
        if criteria == "all" :
            if len(Ferme.animals) < 1 :
                print("You don't have any animals.\nStart by adding some.")
                return None
            
            print(f"You have {len(Ferme.animals)} animals :")
            x = 0
            for animal in Ferme.animals :
                x+=1
                print(f"{x}. {animal.name}, {animal.age} y-o")

            

    def add(newAnimal) :
        try :
            for item in Ferme.animals :
                if item.name == newAnimal.name :
                    print("An animal with the same name already exists.\nBe more creative ;) !")
                    return 'fail'
            Ferme.animals.append(newAnimal)
            return "ok"
        except Exception as err :
            print("Source : Ferme->add() \n"
                f"Error : {err}")
            return "fail"
    
    def crier() :
        print(f"You have {str(len(Ferme.animals))} animals in the farm.")
        try :
            x = 0
            for animal in Ferme.animals :
                x+=1
                print(f"{x}. {animal.name} , {animal.age} years old")
                animal.cri()
            return 'ok'
        except Exception as err :
            print("Source : Ferme->crier() \n"
                f"Error : {err}")
        return None
    

    def kill(animalName) :
        try :
            status = "fail"
            for item in Ferme.animals :
                if (str(item.name).lower()) == (str(animalName).lower()) :
                    Ferme.animals.remove(item)
                    print(f"RIP : {item.name} died.")
                    status = "ok"
            if status == "fail" :
                print(f"No animal with given name <{animalName}> found.")
            return status
            
        except Exception as err :
            print("Source : Ferme->add() \n"
                f"Error : {err}")
            return "fail"