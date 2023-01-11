Ecrivez un programme qui cree une ferme d’animaux. Affichez un menu permettant de :


	
Ajouter un animal, une fois cette option selectionnee vous pouvez selectionner le type d’animal a creer, et enfin lui donnez son nom et son age. Lorsqu’un animal est cree, affichez le message 
le <animal> <nom de l'animal> est né
	
Lancer le cri de tous les animaux de la ferme.
	
Tuer un animal. 
Si vous entrez le nom d’un animal qui n’est pas dans votre ferme, affichez un message l’indiquant, et redemandez a l’utilisateur d’entrer un nom. 
Si vous tuez un animal, affichez le message :
Le <animal> <nom de l'animal> est mort
	
Afficher un message : 
"Ma ferme a n animaux" - n etant le nombre d’animaux dans la ferme.
	
Quitter le programme.
	 


Pour la creation de la ferme:

	
Créez une classe Animal avec les attributs nom (chaine de caractères) et age (entier). La classe doit avoir une méthode cri() qui affiche le cri de l'animal.
	
Créez une classe Chat qui hérite de la classe Animal et qui surcharge la méthode cri() pour afficher "Miaou".
	
Créez une classe Chien qui hérite de la classe Animal et qui surcharge la méthode cri() pour afficher "Ouaf".
	
Créez une classe Ferme avec un attribut animaux qui est une liste d'animaux. La classe doit avoir une méthode ajouter_animal(self, animal) qui permet d'ajouter un animal à la liste, et une méthode crier(self) qui appelle la méthode cri() de chaque animal de la liste.
	
Créez une instance de la classe Ferme et ajoutez-y des chats et des chiens. Appelez la méthode crier() de la ferme et vérifiez que les cris des animaux sont bien affichés.
	
Ajoutez une representation en chaine de caracteres de la ferme. Elle doit afficher “Ferme avec n animaux”, n etant ici le nombre d’animaux dans la ferme

Votre projet devra contenir deux modules au moins: utils.py, qui contiendra la plupart de vos fonctions, et ferme.py, qui contiendra la declaration de vos classes Ferme, Animal, Chien, et Chat.