
class Role(object):

    def __init__(self, name:str, abilities:dict, description:str):
        self.name = name
        self.abilities = abilities
        self.description = description

        def get_name(self):
            return self.name
        def get_abilities(self):
            return self.abilities
        def get_description(self):
            return self.description

        def add_ability(self, ability):
            self.abilities.append(ability)
