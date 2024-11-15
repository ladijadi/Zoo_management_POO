# Définition de la classe Cage
class Cage:
    # Constructeur pour initialiser un objet Cage
    def __init__(self):
        # Liste pour stocker les instances d'animaux
        self.animaux = []

    # Méthode pour ajouter un animal à la cage
    def ajouter_animal(self, animal):
        # Ajoute l'instance d'Animal à la liste `animaux`
        self.animaux.append(animal)

    # Méthode pour afficher la liste des animaux présents dans la cage
    def lister_animaux(self):
        # Vérifie si la liste 'animaux' est vide
        if not self.animaux:
            # Affiche un message si la cage est vide
            print("La cage est vide.")
        else:
            # Itère sur chaque animal de la liste
            for animal in self.animaux:
                # Affiche le nom et l'espèce de l'animal
                print(f"{animal.nom} ({animal.espece})")
