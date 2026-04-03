from role import Role
from item import Item
from ability import Ability
from bisect import bisect_right
from abilityType import AbilityType

class Character(object):

    LEVEL_TABLE = [0, 100, 250, 700, 1450, 3500, 7500, 12000, 20000]
    
    def __init__(self, name: str, experience: int, role: Role, health: int, money: (int, int, int), inventory: list):
        self.name = name
        self.experience = experience
        self.role = role
        self.max_health = health
        self.current_health = self.max_health
        self.money = money
        self.inventory = inventory
        self.shield = 0.0
        
    # Basic Getters and Setters
    def get_name(self) -> str:
        return self.name
    def get_experience(self) -> int:
        return self.experience
    def get_role(self) -> Role:
        return self.role
    def get_max_health(self) -> int:
        return self.max_health
    def get_current_health(self) -> int:
        return self.current_health
    def get_money(self) -> tuple:
        return self.money
    def get_inventory(self) -> list:
        return self.inventory
    def get_level(self) -> int:
        return bisect_right(self.LEVEL_TABLE, self.experience)
    def get_shield(self) -> float:
        return self.shield
    

    def set_name(self, name: str):
        self.name = name
    def set_experience(self, experience: int):
        self.experience = experience
    def set_role(self, role: Role):
        self.role = role
    def set_max_health(self, health: int):
        self.max_health = health
    def set_current_health(self, health: int):
        self.current_health = health
    def set_money(self, money: tuple):
        self.money = money
    def set_inventory(self, inventory: list):
        self.inventory = inventory


    def adjust_shield(self, shield: float):
        self.shield += shield

        
    def add_money(self, gold=0, silver = 0, copper=0):
        """
        A simple function to add money to the character. Use negative values to subtract money.
        :param gold: 
        :param silver: 
        :param copper: 
        :return: 
        """
        self.money[0] += gold
        self.money[1] += silver
        self.money[2] += copper

    def add_item(self, item: Item):
        self.inventory.append(item)

    def remove_item(self, item: Item):
        self.inventory.remove(item)

    def take_damage(self, damage: int) -> bool:
        if damage > 0:
            self.health -= damage
            return True
        else:
            ArithmeticError("Cannot do negative damage")
        return False


    def heal_character(self, effect_amount):
        if effect_amount > 0:
            self.health += effect_amount
            return True
        else:
            ArithmeticError("Cannot do negative effect")
        return False

    def do_action(self, ability: Ability,  target) -> bool:
        """
        Perform abilities action on target
        :param self:
        :param ability: Action to perform
        :param target: The target on which to perform the action
        :return: Bool success or failure
        """

        match ability.type:
            case AbilityType.DAMAGE:
                res = target.take_damage(ability.effect_amount)
                if res:
                    print(f"####CONSOLE-LOG####\n{target.name} took {ability.get_effect_amount()} damage!\n####END-LOG####")
                else:
                    print("####CONSOLE-LOG####\nFailed to apply Damage!\n####END-LOG####")

            case AbilityType.HEALING:
                res = target.heal_character(ability.effect_amount)
                if res:
                    print(f"####CONSOLE-LOG\n{target.name} healed {ability.get_effect_amount()} health!\n####END-LOG####")
                else:
                    print(f"####CONSOLE-LOG\nFailed to apply Health!\n####END-LOG####")

            case AbilityType.DEFENSE:
                target.apply_shield(ability.effect_amount)

            case AbilityType.ROLEPLAY:
                print(ability.action_event)

    def tostring(self):
        print(f'Name: {self.name}\nRole: {self.role.name}\nExperience: {self.experience}\nLevel: {self.get_level()}\nMax Health: {self.health}\nMoney: {self.money}\nInventory: {self.inventory}')




