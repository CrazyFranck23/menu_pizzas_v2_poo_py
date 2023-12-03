
class Pizza:
    def __init__(self, nom, prix, ingredients):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients

    def afficher(self):
        print(f"PIZZA {self.nom} : {self.prix}€")
        print(", ".join(self.ingredients))
        print()

