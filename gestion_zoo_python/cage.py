from animal import Lion, Gazelle, Hyene

class Cage:
    def __init__(self, nom):
        self.nom = nom  # Nom de la cage
        self.animaux = []  # Liste pour stocker les animaux de la cage

    def ajouter_animal(self, animal):
        if animal not in self.animaux:
            self.animaux.append(animal)  # Ajouter un animal à la cage
            print(f"{animal} a été ajouté à la {self.nom}.")
        else:
            print(f"{animal} est déjà dans la {self.nom}.")

    def supprimer_animal(self, animal):
        if animal in self.animaux:
            self.animaux.remove(animal)  # Supprimer un animal de la cage
            print(f"{animal} a été retiré de la {self.nom}.")
        else:
            print(f"{animal} n'est pas dans la {self.nom}.")

    def lister_animaux(self):
        if not self.animaux:
            print(f"La {self.nom} est vide.")
        else:
            print(f"Animaux dans la {self.nom} :")
            for animal in self.animaux:
                print(f" - {animal}")

    def verifier_predation(self):
        victimes = set()
        for predateur in self.animaux:
            for proie in self.animaux:
                if predateur != proie:  # Empêche un animal de s'attaquer lui-même
                    if isinstance(predateur, Lion) and isinstance(proie, (Gazelle, Hyene)):
                        if proie not in victimes:
                            print(f"{predateur} a mangé {proie} !")
                            victimes.add(proie)
        
        # Mise à jour de la liste des animaux après la prédation
        self.animaux = [animal for animal in self.animaux if animal not in victimes]
        if victimes:
            print("La liste des animaux a été mise à jour après la prédation.")
        else:
            print("Aucune prédation n'a eu lieu.")
