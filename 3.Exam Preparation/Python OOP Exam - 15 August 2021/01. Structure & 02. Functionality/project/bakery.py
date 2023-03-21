from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        if name.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")

        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type: str, name: str, price: float):
        if any(food.name == name for food in self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type == "Bread":
            food = Bread(name, price)
        elif food_type == "Cake":
            food = Cake(name, price)
        else:
            return

        self.food_menu.append(food)
        return f"Added {food.name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if any(drink.name == name for drink in self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
        elif drink_type == "Water":
            drink = Water(name, portion, brand)
        else:
            return

        self.drinks_menu.append(drink)
        return f"Added {drink.name} ({drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if any(table.table_number == table_number for table in self.tables_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        else:
            return

        self.tables_repository.append(table)
        return f"Added table number {table.table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = next((table for table in self.tables_repository if not table.is_reserved and table.capacity >= number_of_people), None)

        if table:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        else:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self._find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered_food = []
        not_in_menu = []

        for food_name in food_names:
            food = next((food for food in self.food_menu if food.name == food_name), None)
            if food:
                table.order_food(food)
                ordered_food.append(str(food))
            else:
                not_in_menu.append(food_name)

        response = [f"Table {table_number} ordered:"]
        response.extend(ordered_food)
        if not_in_menu:
            response.append(f"{self.name} does not have in the menu:")
            response.extend(not_in_menu)

        return "\n".join(response)

    def order_drink(self, table_number: int, *drink_names):
        table = self._find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"
            ordered_drinks = []
            not_in_menu = []

            for drink_name in drink_names:
                drink = next((drink for drink in self.drinks_menu if drink.name == drink_name), None)
                if drink:
                    table.order_drink(drink)
                    ordered_drinks.append(str(drink))
                else:
                    not_in_menu.append(drink_name)

            response = [f"Table {table_number} ordered:"]
            response.extend(ordered_drinks)
            if not_in_menu:
                response.append(f"{self.name} does not have in the menu:")
                response.extend(not_in_menu)

            return "\n".join(response)

    def leave_table(self, table_number: int):
        table = self._find_table(table_number)
        if not table:
            return

        bill = table.get_bill()
        self.total_income += bill
        table.clear()

        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        free_tables_info = [table.free_table_info() for table in self.tables_repository if not table.is_reserved]
        return "\n".join(free_tables_info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def _find_table(self, table_number):
        return next((table for table in self.tables_repository if table.table_number == table_number), None)
