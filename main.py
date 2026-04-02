from character import Character
from item import Item
from role import Role
from ability import Ability

def main():
    wizard = Role("Wizard", {}, "Those who study the mysteries of the arcane to control the universe call themselves Wizards.")
    john = Character("john", 2200, wizard, {}, (32, 16, 8), [])
    print(john.tostring())


if __name__ == '__main__':
    main()
