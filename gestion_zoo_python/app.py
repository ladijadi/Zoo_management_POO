from zoo import Zoo
from animal import Lion, Gazelle, Hyene
from cage import Cage

class Animal:
    def __init__(self, nom, type_animal):
        self.nom = nom
        self.type_animal = type_animal

    # Méthode pour nourrir un animal
    def nourrir(self, nourriture):
        print(f"{self.nom} a mangé {nourriture}.")

class Cage:
    def __init__(self, nom):
        self.nom = nom
        self.animaux = []

    # Méthode pour ajouter un animal à la cage
    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    # Méthode pour supprimer un animal de la cage
    def supprimer_animal(self, animal):
        self.animaux.remove(animal)

    # Méthode pour lister les animaux dans la cage
    def lister_animaux(self):
        if not self.animaux:
            print(f"Aucun animal dans la {self.nom}.")
        else:
            for animal in self.animaux:
                print(f" - {animal.type_animal} ({animal.nom})")

class Zoo:
    def __init__(self):
        self.cages = []

    def ajouter_cage(self, cage):
        self.cages.append(cage)

    def compter_cages(self):
        return len(self.cages)

    def afficher_cages(self):
        print(f"Le zoo contient {self.compter_cages()} cage(s).")
        for i, cage in enumerate(self.cages, start=1):
            print(f"Cage {i}:")
            cage.lister_animaux()

    def afficher_animaux_dans_cages(self):
        for i, cage in enumerate(self.cages, start=1):
            print(f"Contenu de la {cage.nom}:")
            cage.lister_animaux()
            print("")

    def nourrir_animal(self, cage_num, animal_nom, nourriture):
        if 0 < cage_num <= len(self.cages):  # Assurez-vous que cage_num est un entier
            cage = self.cages[cage_num - 1]  # Accéder à la cage par son numéro
            for animal in cage.animaux:
                if animal.nom == animal_nom:
                    animal.nourrir(nourriture)
                    return
            print(f"Aucun animal avec le nom {animal_nom} dans cette cage.")
        else:
            print("Numéro de cage invalide.")

  
    def simuler_predation(self, predator_nom, prey_nom):
    # On va chercher à la fois le prédateur et la proie dans le zoo entier
        predator = None
        prey = None

        # Recherche des animaux dans toutes les cages
        for cage in self.cages:
            for animal in cage.animaux:
                if animal.nom == predator_nom:
                    predator = animal
                if animal.nom == prey_nom:
                    prey = animal

        # Si les deux animaux ont été trouvés et sont dans la même cage
        if predator and prey:
            # Vérification si le prédateur et la proie sont dans la même cage
            for cage in self.cages:
                if predator in cage.animaux and prey in cage.animaux:
                    print(f"{predator_nom} a mangé {prey_nom} !")
                    cage.supprimer_animal(prey)
                    return
            print(f"{predator_nom} et {prey_nom} ne sont pas dans la même cage.")
        else:
            print(f"Prédation entre {predator_nom} et {prey_nom} impossible. L'un des deux n'a pas été trouvé.")

# Création d'animaux
lion = Animal("Simba", "Lion")
gazelle = Animal("Gazou", "Gazelle")
hyene = Animal("Shenzi", "Hyène")

# Création de cages
cage1 = Cage("Cage 1")
cage2 = Cage("Cage 2")
cage3 = Cage("Cage 3")

# Ajout des animaux dans les cages
cage1.ajouter_animal(lion)
cage2.ajouter_animal(gazelle)
cage3.ajouter_animal(hyene)

# Création du zoo
zoo = Zoo()
zoo.ajouter_cage(cage1)
zoo.ajouter_cage(cage2)
zoo.ajouter_cage(cage3)

# Menu interactif
while True:
    print("\nMenu:")
    print("1. Afficher les cages")
    print("2. Afficher les animaux dans chaque cage")
    print("3. Nourrir un animal")
    print("4. Simuler une prédation")
    print("5. Quitter")

    choix = input("Choisissez une option (1-5): ")

    if choix == "1":
        zoo.afficher_cages()
    elif choix == "2":
        zoo.afficher_animaux_dans_cages()
    elif choix == "3":
        cage_num = int(input("Numéro de la cage : "))
        animal_nom = input("Nom de l'animal à nourrir : ")
        nourriture = input("Nourriture : ")
        zoo.nourrir_animal(cage_num, animal_nom, nourriture)
    elif choix == "4":
        predator_nom = input("Nom du prédateur : ")
        prey_nom = input("Nom de la proie : ")
        zoo.simuler_predation(predator_nom, prey_nom)
    elif choix == "5":
        print("Merci d'avoir utilisé le zoo de gestion!")
        break
    else:
        print("Option invalide. Essayez à nouveau.")