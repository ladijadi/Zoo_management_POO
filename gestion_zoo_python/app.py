# Importation des classes définies dans d'autres fichiers
from zoo import Zoo
from cage import Cage
from animal import Lion, Gazelle, Hyene, Serpent

# Fonction principale pour exécuter le programme
def main():
    # Création d'une instance de Zoo
    zoo = Zoo()

    # Création de quelques cages
    cage1 = Cage()
    cage2 = Cage()

    # Ajout des cages au zoo
    zoo.ajouter_cage(cage1)
    zoo.ajouter_cage(cage2)

    # Affichage du nombre de cages dans le zoo
    zoo.afficher_cages()

    # Ajout d'animaux dans la première cage
    lion = Lion("Simba")
    gazelle = Gazelle("Gazou")
    hyene = Hyene("Scar")
    
    # Ajout de ces animaux dans la cage 1
    cage1.ajouter_animal(lion)
    cage1.ajouter_animal(gazelle)
    cage1.ajouter_animal(hyene)

    # Ajout d'un serpent dans la deuxième cage
    serpent = Serpent("Kaa")
    cage2.ajouter_animal(serpent)

    # Affichage des animaux présents dans chaque cage
    print("\nListe des animaux dans chaque cage :")
    zoo.afficher_cages()

# Point d'entrée du programme
if __name__ == "__main__":
    # Appel de la fonction principale pour démarrer l'application
    main()