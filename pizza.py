
class Pizza:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def afficher(self):
        print(f"PIZZA {self.nom} : {self.prix}€")
