class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return "Pizza {} already prepared, and we can't make any changes!".format(self.name)

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity * quantity
        else:
            self.ingredients[ingredient] = quantity
            self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return "Pizza {} already prepared, and we can't make any changes!".format(self.name)

        if ingredient not in self.ingredients:
            return "Wrong ingredient selected! We do not use {} in {}!".format(ingredient, self.name)

        if quantity > self.ingredients[ingredient]:
            return "Please check again the desired quantity of {}!".format(ingredient)

        self.ingredients[ingredient] -= quantity
        self.price -= price_per_quantity * quantity

    def make_order(self):
        if self.ordered:
            return "Pizza {} already prepared, and we can't make any changes!".format(self.name)

        self.ordered = True
        return "You've ordered pizza {} prepared with {} and the price will be {}lv.".format(
            self.name, ", ".join("{}: {}".format(ingr, qty) for ingr, qty in self.ingredients.items()), self.price
        )


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
