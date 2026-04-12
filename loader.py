import yaml
from pathlib import Path
from character import Character
from role import Role
from ability import Ability, AbilityType



def load_file(filename) -> dict:

    with open(filename, 'r') as f:
        return yaml.safe_load(f)

def load_all_files(path: str) -> list:
    path = Path(path)
    ret = []
    yaml_files = sorted(path.glob('*.yaml'))

    for filename in yaml_files:
        ret.append(load_file(filename))
    return ret


def load_character(path: str) -> Character:
    path = Path(path)
    character_stats = load_file(path)
    fireball = Ability(
        'fireball',
        'launch a ball of fire to explode in a large area',
        AbilityType.DAMAGE,
        150,
        'fire',
        effect_amount=23
    )
    role = Role(character_stats['role'], [fireball], "Wizardly magic stuff")
    return Character(character_stats['name'], character_stats['experience'], role, character_stats['health'], type(character_stats['money']), character_stats['inventory'])