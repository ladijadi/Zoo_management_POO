# Zoo_management_POO

Gestionnaire de Zoo est une application en ligne de commande qui permet de simuler la gestion d'un zoo en utilisant la Programmation Orientée Objet (POO). Cette application offre des fonctionnalités pour ajouter des cages, gérer des animaux et visualiser le contenu du zoo.

## Table des matières

Présentation du projet

Fonctionnalités

Technologies utilisées

Installation

Utilisation

Structure des fichiers

Améliorations futures

Contribuer

Licence

## Présentation du projet
Gestionnaire de Zoo est conçu pour permettre aux utilisateurs de gérer un zoo virtuel. Le projet met en pratique les concepts de POO, tels que l'encapsulation, l'héritage et le polymorphisme, pour structurer le code de manière efficace. Les utilisateurs peuvent ajouter des cages, insérer des animaux dans les cages et consulter la liste des animaux présents.

## Fonctionnalités
Ajout de cages : Permet d'ajouter des cages au zoo et de consulter le nombre de cages.
Ajout d'animaux : Les animaux peuvent être ajoutés à des cages avec un nom personnalisé.
Liste des animaux : Affiche la liste des animaux présents dans chaque cage.
Bonus : Gestion des relations prédateur/proie : Simule des interactions où certains animaux chassent d'autres espèces.
Bonus : Alimentation des animaux : Vérifie le régime alimentaire des animaux et affiche un message si l'alimentation est appropriée ou non.

## Technologies utilisées
Langage : Python
Outils : Visual Studio Code (VSCode)
Paradigme : Programmation Orientée Objet (POO)
Installation
Cloner le dépôt : git clone https://github.com/votre-nom-utilisateur/gestionnaire-de-zoo.git
                  cd gestionnaire-de-zoo
                  Créer un environnement virtuel et l'activer : python3 -m venv venv
                                                                source venv/bin/activate  # Sur Windows, utilisez venv\Scripts\activate
                  Installer les dépendances : pip install -r requirements.txt


## Utilisation
Pour exécuter le programme, lancez le script principal :
python main.py

## Structure des fichiers

gestionnaire-de-zoo/
│
├── animal.py          # Définition de la classe Animal et ses sous-classes
├── cage.py            # Classe Cage, gestion des animaux dans une cage
├── zoo.py             # Classe Zoo, gestion globale du zoo
├── main.py            # Script principal pour exécuter le programme
├── requirements.txt   # Liste des dépendances (si nécessaire)
└── README.md          # Documentation du projet

## Améliorations futures

Interface graphique : Ajouter une interface utilisateur pour rendre l'application plus intuitive.
Système de sauvegarde : Implémenter un système pour sauvegarder l'état du zoo dans un fichier.
Statistiques avancées : Intégrer des statistiques sur les animaux et les cages.

## Contribuer
Les contributions sont les bienvenues ! Pour contribuer, veuillez créer une issue ou un pull request.

## Licence
Ce projet est sous licence MIT.

Cela devrait te donner une base solide pour ton README. Tu pourras l'adapter au fur et à mesure que ton projet évolue.