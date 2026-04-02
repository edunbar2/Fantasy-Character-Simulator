import enum

import character


class AbilityType(enum.Enum):
    DAMAGE = 1
    HEALING = 2
    DEFENSE = 3
    ROLEPLAY = 4



class Ability:
    def __init__(self, name: str, description: str, type: str, range: int, damage_type: str, effect_amount=None, action_event=None):
        self.name = name
        self.description = description
        self.type = type
        self.range = range
        self.damage_type = damage_type
        self.effect_amount = effect_amount
        self.action_event = action_event

        def get_name(self):
            return self.name
        def get_type(self):
            return self.type
        def get_range(self):
            return self.range
        def get_damage_type(self):
            return self.damage_type
        def get_description(self):
            return self.description
        def get_effect_amount(self):
            return self.effect_amount


        def do_action(self, target: character.Character) -> bool:
            """
            Perform abilities action on target
            :param self:
            :param target: The target on which to perform the action
            :return: Bool success or failure
            """

            match self.type:
                case AbilityType.DAMAGE:
                    res = target.take_damage(self.effect_amount)
                    if res:
                        print(f"####CONSOLE-LOG####\n{target.name} took {effect_amount} damage!\n####END-LOG####")
                    else:
                        print("####CONSOLE-LOG####\nFailed to apply Damage!\n####END-LOG####")

                case AbilityType.HEALING:
                    target.heal_character(self.effect_amount)

                case AbilityType.DEFENSE:
                    target.apply_shield(self.effect_amount)

                case AbilityType.ROLEPLAY:
                    print(self.action_event)
