class Animal:
    def __init__(self, nom):
        self.nom = nom  # Nom de l'animal
        self.espece = self.__class__.__name__  # Espèce basée sur le nom de la classe (Lion, Gazelle, etc.)

    def __str__(self):
        return f"{self.espece} ({self.nom})"

    def nourrir(self, aliment):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")

class Lion(Animal):
    def __init__(self, nom):
        super().__init__(nom)
        self.regime = "carnivore"

    def nourrir(self, aliment):
        if aliment == "viande":
            print(f"{self.nom} le {self.espece} a été nourri avec de la viande.")
        else:
            print(f"{self.nom} le {self.espece} ne mange pas cet aliment.")

class Gazelle(Animal):
    def __init__(self, nom):
        super().__init__(nom)
        self.regime = "herbivore"

    def nourrir(self, aliment):
        if aliment == "plantes":
            print(f"{self.nom} la {self.espece} a été nourrie avec des plantes.")
        else:
            print(f"{self.nom} la {self.espece} ne mange pas cet aliment.")

class Hyene(Animal):
    def __init__(self, nom):
        super().__init__(nom)
        self.regime = "omnivore"

    def nourrir(self, aliment):
        if aliment in ["viande", "plantes"]:
            print(f"{self.nom} la {self.espece} a été nourrie avec {aliment}.")
        else:
            print(f"{self.nom} la {self.espece} ne mange pas cet aliment.")