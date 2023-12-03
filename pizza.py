
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


class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2

    def __init__(self, prix=PRIX_DE_BASE):
        super().__init__("Personnalisée", prix, [])
        self.demander_ingredients_utilisateur()
        self.calculer_le_prix()

    def demander_ingredients_utilisateur(self):
        while True:
            ingredient = input("Ajoutez un ingrédient (ou ENTER pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")

    def calculer_le_prix(self):
        self.prix = self.PRIX_DE_BASE + (self.PRIX_PAR_INGREDIENT*len(self.ingredients))
