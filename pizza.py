
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
    dernier_numero = 0

    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.num_pizza = PizzaPersonnalisee.dernier_numero  # Quand une pizzaPerso sera cree, elle prendra auto le num 1
        super().__init__("Personnalisée " + str(self.num_pizza), 0, [])
        # self.num_pizza = num_pizza
        self.demander_ingredients_utilisateur()
        self.calculer_le_prix()

    def demander_ingredients_utilisateur(self):
        print()
        print("Ingredients pour la pizza personnalisée", self.num_pizza)
        while True:
            ingredient = input("Ajoutez un ingrédient (ou ENTER pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")

    def calculer_le_prix(self):
        self.prix = self.PRIX_DE_BASE + (self.PRIX_PAR_INGREDIENT*len(self.ingredients))
