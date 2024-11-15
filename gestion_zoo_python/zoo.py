# Définition de la classe Zoo
class Zoo:
    # Constructeur pour initialiser un objet Zoo
    def __init__(self):
        # Liste pour stocker les instances de cages
        self.cages = []

    # Méthode pour ajouter une cage au zoo
    def ajouter_cage(self, cage):
        # Ajoute l'instance de Cage à la liste `cages`
        self.cages.append(cage)

    # Méthode pour compter le nombre de cages dans le zoo
    def compter_cages(self):
        # Retourne le nombre de cages
        return len(self.cages)

    # Méthode pour afficher les cages et leur contenu
    def afficher_cages(self):
        # Affiche le nombre total de cages
        print(f"Le zoo contient {self.compter_cages()} cage(s).")
        # Itère sur chaque cage avec son index
        for i, cage in enumerate(self.cages, start=1):
            # Affiche le numéro de la cage
            print(f"Cage {i}:")
            # Appelle la méthode pour lister les animaux dans la cage
            cage.lister_animaux()
