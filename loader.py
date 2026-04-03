import yaml
from pathlib import Path

class Loader():
    def __init__(self, path: str):
        self.path = Path(path)

    def load_file(self, filename) -> dict:

        with open(filename, 'r') as f:
            return yaml.safe_load(f)

    def load_all_files(self, ) -> list:
        ret = []
        yaml_files = sorted(self.path.glob('*.yaml'))

        for filename in yaml_files:
            ret.append(self.load_file(filename))
        return ret