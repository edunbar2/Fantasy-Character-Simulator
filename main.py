from character import Character, AbilityType
from item import Item
from role import Role
from ability import Ability

def main():
    fireball = Ability(
        'fireball',
        'launch a ball of fire to explode in a large area',
        AbilityType.DAMAGE,
        'fire',
        150,
        effect_amount=23
    )
    wizard = Role(
        "Wizard",
        [fireball],
        "Those who study the mysteries of the arcane to control reality around them call themselves Wizards."
    )
    john = Character("john", 2200, wizard, {}, (32, 16, 8), [])
    print(john.tostring())
    print("####CONSOLE-LOG####\nCasting Fireball on John!\n####END-LOG####")
    john.do_action(fireball, john)
    print(john.tostring())


if __name__ == '__main__':
    main()
