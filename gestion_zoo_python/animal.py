# Définition de la classe de base Animal
class Animal:
    # Constructeur pour initialiser un objet Animal
    def __init__(self, nom, espece):
        # Attribut pour stocker le nom de l'animal
        self.nom = nom
        # Attribut pour stocker l'espèce de l'animal
        self.espece = espece

    # Méthode spéciale pour retourner une chaîne représentant l'objet
    def __str__(self):
        # Retourne le nom et l'espèce de l'animal
        return f"{self.nom} ({self.espece})"

# Sous-classe de Animal pour représenter un lion
class Lion(Animal):
    # Constructeur de la classe Lion
    def __init__(self, nom):
        # Appelle le constructeur de la classe parente avec "Lion" comme espèce
        super().__init__(nom, "Lion")

# Sous-classe de Animal pour représenter une gazelle
class Gazelle(Animal):
    # Constructeur de la classe Gazelle
    def __init__(self, nom):
        # Appelle le constructeur de la classe parente avec "Gazelle" comme espèce
        super().__init__(nom, "Gazelle")

# Sous-classe de Animal pour représenter une hyène
class Hyene(Animal):
    # Constructeur de la classe Hyène
    def __init__(self, nom):
        # Appelle le constructeur de la classe parente avec "Hyène" comme espèce
        super().__init__(nom, "Hyène")

# Sous-classe de Animal pour représenter un serpent
class Serpent(Animal):
    # Constructeur de la classe Serpent
    def __init__(self, nom):
        # Appelle le constructeur de la classe parente avec "Serpent" comme espèce
        super().__init__(nom, "Serpent")
