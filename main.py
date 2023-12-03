from pizza import Pizza

# veggie ;
#    By default -> False
#    True -> La Pizza est végétarienne

pizzas = (Pizza("Cannibale", 12.6, ("viande hachée", "poulet roti", "merguez", "mozzarella")),
          Pizza("Savoyarde", 10.2, ("mozzarella", "lardons fumés", "pomme de terre", "reblochon")),
          Pizza("Végétarienne", 7.8, ("champignons", "tomates", "oignons", "poivrons"), True),
          Pizza("Hot & Spicy", 11.3, ("piment jalapenos", "merguez", "tomates", "duo de poivrons")),
          Pizza("4 Fromages", 8.5, ("brie", "emmental", "compté", "parmessan"), True))

for pizza in pizzas:
    pizza.afficher()
