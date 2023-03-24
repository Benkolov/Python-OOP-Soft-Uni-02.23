from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_names = []
        for player in players:
            if player in self.players:
                continue
            self.players.append(player)
            added_names.append(player.name)
        return f"Successfully added: {', '.join(added_names)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def find_supply(self, supply_type):
        for supply in reversed(self.supplies):
            if isinstance(supply, supply_type):
                self.supplies.remove(supply)
                return supply
        return None

    def sustain(self, player_name, sustenance_type):
        player = next((p for p in self.players if p.name == player_name), None)
        if not player:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        supply_type = None
        if sustenance_type == "Food":
            supply_type = Food
        elif sustenance_type == "Drink":
            supply_type = Drink

        if not supply_type:
            return

        supply = self.find_supply(supply_type)
        if not supply:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(player.stamina + supply.energy, 100)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name, second_player_name):
        first_player = next((p for p in self.players if p.name == first_player_name), None)
        second_player = next((p for p in self.players if p.name == second_player_name), None)

        error_message = ''
        if first_player.stamina == 0:
            error_message += f"Player {first_player.name} does not have enough stamina."

        if second_player.stamina == 0:
            error_message += '\n' + f"Player {second_player.name} does not have enough stamina."

        if error_message:
            return error_message

        first_attacker, second_attacker = (
            first_player, second_player) if first_player.stamina < second_player.stamina else (
            second_player, first_player)

        damage = first_attacker.stamina / 2
        second_attacker.stamina = max(second_player.stamina - damage, 0)
        if second_attacker.stamina == 0:
            return f"Winner: {first_attacker.name}"

        damage = second_attacker.stamina / 2
        first_attacker.stamina = max(first_player.stamina - damage, 0)
        if first_player.stamina == 0:
            return f"Winner: {second_attacker.name}"

        winner = first_attacker if first_attacker.stamina > second_attacker.stamina else second_attacker
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina -= player.age * 2
            player.stamina = max(0, player.stamina)

        food_supply = self.find_supply(Food)
        drink_supply = self.find_supply(Drink)

        for player in self.players:
            if player.need_sustenance and food_supply:
                player.stamina = min(player.stamina + food_supply.energy, 100)
                food_supply = self.find_supply(Food)

            if player.need_sustenance and drink_supply:
                player.stamina = min(player.stamina + drink_supply.energy, 100)
                drink_supply = self.find_supply(Drink)

    def __str__(self):
        players_info = "\n".join(str(player) for player in self.players)
        supplies_info = "\n".join(supply.details() for supply in self.supplies)
        return f"{players_info}\n{supplies_info}"
