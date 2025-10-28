import json

from chore_tracker.chore import Chore2


class Data:
    def __init__(self, file_name, chores):
        self.file_name = file_name
        self.chores = chores


    def load_chores(file_name: str) -> list:
        try:
            with open(file_name) as f:
                items = json.load(f)
                chores = [Chore2.from_dict(item) for item in items]

        except Exception as error:
            print(error)
            chores = []

        return chores

    def save_chores(chores: list, file_name):
        with open(file_name, 'w') as f:
            json.dump([chore.as_dict() for chore in chores], f)