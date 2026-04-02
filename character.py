from role import Role
from item import Item
from ability import Ability

from bisect import bisect_right

class Character(object):

    LEVEL_TABLE = [0, 100, 250, 700, 1450, 3500, 7500, 12000, 20000]
    
    def __init__(self, name: str, experience: int, role: Role, health: int, money: (int, int, int), inventory: list):
        self.name = name
        self.experience = experience
        self.role = role
        self.health = health
        self.money = money
        self.inventory = inventory
        
    # Basic Getters and Setters
    def get_name(self) -> str:
        return self.name
    def get_experience(self) -> int:
        return self.experience
    def get_role(self) -> Role:
        return self.role
    def get_health(self) -> int:
        return self.health
    def get_money(self) -> tuple:
        return self.money
    def get_inventory(self) -> list:
        return self.inventory
    def get_level(self) -> int:
        return bisect_right(self.LEVEL_TABLE, self.experience)
    

    def set_name(self, name: str):
        self.name = name
    def set_experience(self, experience: int):
        self.experience = experience
    def set_role(self, role: Role):
        self.role = role
    def set_health(self, health: int):
        self.health = health
    def set_money(self, money: tuple):
        self.money = money
    def set_inventory(self, inventory: list):
        self.inventory = inventory
        
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

    def tostring(self):
        print(f'Name: {self.name}\nRole: {self.role.name}\nExperience: {self.experience}\nLevel: {self.get_level()}\nMax Health: {self.health}\nMoney: {self.money}\nInventory: {self.inventory}')




