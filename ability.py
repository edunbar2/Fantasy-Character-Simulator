from abilityType import AbilityType

class Ability:
    def __init__(self, name: str, description: str, type: AbilityType, range: int, effect_type: str, effect_amount=None, action_event=None):
        self.name = name
        self.description = description
        self.type = type
        self.range = range
        self.effect_type = effect_type
        self.effect_amount = effect_amount
        self.action_event = action_event

    def get_name(self):
        return self.name
    def get_type(self):
        return self.type
    def get_range(self):
        return self.range
    def get_effect_type(self):
        return self.effect_type
    def get_description(self):
        return self.description
    def get_effect_amount(self):
        return self.effect_amount


