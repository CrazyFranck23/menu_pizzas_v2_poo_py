
class Pizza:
    def __init__(self, nom, prix, ingredients, veggie: bool = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.veggie = veggie

    def afficher(self):
        message = f"PIZZA {self.nom} : {self.prix}€ "
        if self.veggie:
            message += "- VEGETARIENNE"
        print(message)
        print(", ".join(self.ingredients))

        print()


# MAIN

