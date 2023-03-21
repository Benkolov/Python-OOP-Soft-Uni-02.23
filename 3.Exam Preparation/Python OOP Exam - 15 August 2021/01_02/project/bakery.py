from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type: str, name: str, price: float):
        if any(f.name == name for f in self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type == "Bread":
            food = Bread(name, price)
        elif food_type == "Cake":
            food = Cake(name, price)
        else:
            raise ValueError("Invalid food type!")

        self.food_menu.append(food)
        return f"Added {food.name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if any(d.name == name for d in self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
        elif drink_type == "Water":
            drink = Water(name, portion, brand)
        else:
            raise ValueError("Invalid drink type!")

        self.drinks_menu.append(drink)
        return f"Added {drink.name} ({drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if any(t.table_number == table_number for t in self.tables_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        else:
            raise ValueError("Invalid table type!")

        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = next((t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people), None)
        if table is None:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):
        table = self._find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_food = []
        not_in_menu = []
        for food_name in food_names:
            food = self._find_food_by_name(food_name)
            if food is None:
                not_in_menu.append(food_name)
            else:
                ordered_food.append(food)
                table.order_food(food)

        result = [f"Table {table_number} ordered:"]
        result.extend([str(f) for f in ordered_food])
        if not_in_menu:
            result.append(f"{self.name} does not have in the menu:")
            result.extend(not_in_menu)
        return "\n".join(result)

    def order_drink(self, table_number: int, *drink_names: str):
        table = self._find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_drinks = []
        not_in_menu = []
        for drink_name in drink_names:
            drink = self._find_drink_by_name(drink_name)
            if drink is None:
                not_in_menu.append(drink_name)
            else:
                ordered_drinks.append(drink)
                table.order_drink(drink)

        result = [f"Table {table_number} ordered:"]
        result.extend([str(d) for d in ordered_drinks])
        if not_in_menu:
            result.append(f"{self.name} does not have in the menu:")
            result.extend(not_in_menu)
        return "\n".join(result)

    def leave_table(self, table_number: int):
        table = self._find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        free_tables = [t.free_table_info() for t in self.tables_repository if not t.is_reserved]
        return "\n".join(free_tables)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def _find_table_by_number(self, table_number: int):
        return next((t for t in self.tables_repository if t.table_number == table_number), None)

    def _find_food_by_name(self, food_name: str):
        return next((f for f in self.food_menu if f.name == food_name), None)

    def _find_drink_by_name(self, drink_name: str):
        return next((d for d in self.drinks_menu if d.name == drink_name), None)