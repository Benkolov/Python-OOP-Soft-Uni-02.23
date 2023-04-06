from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, (Starter, MainDish, Dessert)):
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return "\n".join([meal.details() for meal in self.menu])

    def find_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client
        return None

    def find_meal(self, meal_name: str):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal
        return None

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self.find_client(client_phone_number)
        if client is None:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        ordered_meals = []
        for meal_name, quantity in meal_names_and_quantities.items():
            meal = self.find_meal(meal_name)
            if meal is None:
                raise Exception(f"{meal_name} is not on the menu!")

            if meal.quantity < quantity:
                meal_type = type(meal).__name__
                raise Exception(f"Not enough quantity of {meal_type}: {meal_name}!")

            ordered_meals.append((meal, quantity))

        for meal, quantity in ordered_meals:
            client.shopping_cart.append(meal)
            client.bill += meal.price * quantity
            meal.quantity -= quantity

        meal_names = ', '.join([meal.name for meal, _ in ordered_meals])
        return f"Client {client_phone_number} successfully ordered {meal_names} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str) -> str:
        client = self.find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            meal.quantity += 1

        client.shopping_cart.clear()
        client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str) -> str:
        client = self.find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.shopping_cart.clear()
        client.bill = 0.0

        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
