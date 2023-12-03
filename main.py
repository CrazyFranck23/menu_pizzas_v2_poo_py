from pizza import Pizza

pizzas = (Pizza("Cannibale", 12.6, ("viande hachée", "poulet roti", "merguez", "mozzarella")),
          Pizza("Savoyarde", 10.2, ("mozzarella", "lardons fumés", "pomme de terre", "reblochon")),
          Pizza("Hot & Spicy", 11.3, ("piment jalapenos", "merguez", "tomates", "duo de poivrons")),
          Pizza("4 Fromages", 8.5, ("brie", "emmental", "compté", "parmessan")),
          Pizza("Végétarienne", 8.5, ("champignons", "tomates", "oignons", "poivrons")))

for pizza in pizzas:
    pizza.afficher()

