class Animal:
    def __init__(self, nom, type_animal):
        self.nom = nom  # Nom de l'animal
        self.espece = self.__class__.__name__  # Espèce basée sur le nom de la classe (Lion, Gazelle, etc.)
        self.type = type_animal  # Carnivore, Herbivore, etc.
        self.nourriture = None  # Nourriture donnée à l'animal

    def __str__(self):
        return f"{self.espece} ({self.nom})"

    def nourrir(self, nourriture):
        self.nourriture = nourriture  # Affecter la nourriture à l'attribut
        print(f"{self.nom} a été nourri avec {self.nourriture}.")

    def predation(self, cible):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")

# Dans la classe Lion
class Lion(Animal):
    def __init__(self, nom):
        super().__init__(nom, "carnivore")
    
    def nourrir(self, nourriture):
        super().nourrir(nourriture)  # Appeler la méthode de la classe parent
    
    def predation(self, cible):
        if cible.type == "herbivore":
            return f"{self.nom} a attaqué et mangé {cible.nom} la {cible.espece}!"
        return f"{self.nom} ne peut pas attaquer {cible.nom}, ils sont du même type."

# Dans la classe Gazelle
class Gazelle(Animal):
    def __init__(self, nom):
        super().__init__(nom, "herbivore")

    def nourrir(self, nourriture):
        super().nourrir(nourriture)

    def predation(self, cible):
        return f"{self.nom} est une proie, elle n'attaque pas !"

# Dans la classe Hyene
class Hyene(Animal):
    def __init__(self, nom):
        super().__init__(nom, "carnivore")

    def nourrir(self, nourriture):
        super().nourrir(nourriture)

    def predation(self, cible):
        if cible.type == "herbivore":
            return f"{self.nom} a attaqué et mangé {cible.nom} la {cible.espece}!"
        return f"{self.nom} ne peut pas attaquer {cible.nom}, ils sont du même type."

# Exemple d'utilisation :
lion1 = Lion("Simba")
gazelle1 = Gazelle("Gazou")
hyene1 = Hyene("Shenzi")

# Nourrir les animaux
lion1.nourrir("viande")
gazelle1.nourrir("plantes")
hyene1.nourrir("viande")

# Simulation de prédation
print(lion1.predation(gazelle1))  # Attaque d'un lion sur une gazelle
print(hyene1.predation(gazelle1))  # Attaque d'une hyène sur une gazelle