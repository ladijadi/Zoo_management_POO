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

    # Méthode pour simuler une prédation
    def simuler_predation(self, predator_nom, prey_nom):
        for cage in self.cages:
            for animal in cage.animaux:
                if animal.nom == predator_nom:
                    for proie in cage.animaux:
                        if proie.nom == prey_nom:
                            print(f"{predator_nom} a mangé {prey_nom} !")
                            cage.supprimer_animal(proie)
                            return
        print(f"Prédation entre {predator_nom} et {prey_nom} impossible. L'un des deux n'a pas été trouvé.")
