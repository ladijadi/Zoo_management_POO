class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def __str__(self):
        return f"{self.espece} nommé {self.nom}"
