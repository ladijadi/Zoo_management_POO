# Importation des classes nécessaires
from animal import Lion, Gazelle, Hyene

class Cage:
    def __init__(self):
        self.animaux = []  # Liste pour stocker les animaux de la cage

    def ajouter_animal(self, animal):
        self.animaux.append(animal)  # Ajouter un animal à la cage

    def lister_animaux(self):
        if not self.animaux:
            print("La cage est vide.")
        else:
            print("Animaux dans la cage :")
            for animal in self.animaux:
                print(f" - {animal}")

    def verifier_predation(self):
        # Ensemble pour garder trace des proies déjà identifiées
        victimes = set()
        for predateur in self.animaux:
            for proie in self.animaux:
                if isinstance(predateur, Lion) and isinstance(proie, Gazelle):
                    if proie not in victimes:
                        print(f"{predateur} a mangé {proie} !")
                        victimes.add(proie)
                elif isinstance(predateur, Lion) and isinstance(proie, Hyene):
                    if proie not in victimes:
                        print(f"{predateur} a mangé {proie} !")
                        victimes.add(proie)
        # Supprimer les proies de la liste des animaux
        self.animaux = [animal for animal in self.animaux if animal not in victimes]