from pizza import *

# veggie ;
#    By default -> False
#    True -> La Pizza est végétarienne

pizzas = [Pizza("Cannibale", 12.6, ("viande hachée", "poulet roti", "merguez")),
          Pizza("Savoyarde", 10.2, ("mozzarella", "lardons fumés", "pomme de terre", "reblochon", "origan")),
          Pizza("Végétarienne", 7.8, ("champignons", "tomates", "oignons", "poivrons"), True),
          Pizza("Hot & Spicy", 11.3, ("piment jalapenos", "merguez", "tomates", "duo de poivrons")),
          Pizza("4 Fromages", 8.5, ("brie", "emmental", "compté", "parmessan"), True),
          PizzaPersonnalisee()]

for pizza in pizzas:
    pizza.afficher()

# ------ FILTRES ------ #
"""
for pizza in pizzas:
    if pizza.prix < 10:  # Condition pour n'afficher que les Pizzas à moins de 10€
        pizza.afficher()
"""

"""
for pizza in pizzas:
    if "tomates" in pizza.ingredients:  # Condition pour n'afficher que les Pizzas contennant des tomates
        pizza.afficher()
"""

"""
for pizza in pizzas:
    if pizza.veggie:  # Condition pour n'afficher que les Pizzas végétarienne # Ajoute le if not pour afficher les non veggie
        pizza.afficher() 
"""

# ------ TRI PIZZA ------ #
"""
def tri(e):
    return e.nom  # L'element e dans ma liste de pizzas c'est bien une Pizza - Ici on tri le nom avec ".nom"
    # return e.prix  # Ici on tri en fonction du prix
    # return len(e.ingredients)  # Triage par nombre d'ingredients

pizzas.sort(key=tri)
"""