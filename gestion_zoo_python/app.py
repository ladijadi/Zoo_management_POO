# Importation des classes nécessaires
from zoo import Zoo
from animal import Lion, Gazelle, Hyene
from cage import Cage

# Création d'instances d'animaux
lion1 = Lion("Simba")
gazelle1 = Gazelle("Gazou")
hyene1 = Hyene("Shenzi")

# Création d'une cage et ajout des animaux
cage1 = Cage()
cage1.ajouter_animal(lion1)
cage1.ajouter_animal(gazelle1)
cage1.ajouter_animal(hyene1)

# Liste des animaux dans la cage
print("Liste des animaux avant la prédation :")
cage1.lister_animaux()

# Vérification des interactions prédateur/proie
print("\nVérification des interactions prédateur/proie :")
cage1.verifier_predation()

# Liste des animaux après la prédation
print("\nListe des animaux après la prédation :")
cage1.lister_animaux()

# Nourrissage des animaux
print("\nNourrissage des animaux :")
lion1.nourrir("viande")
gazelle1.nourrir("plantes")
hyene1.nourrir("plantes")  # Cette ligne devrait indiquer un mauvais choix de nourriture