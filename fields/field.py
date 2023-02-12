from animals.abstract_classes import Animal
from plants.plant import Plant
import json

class Field:
    def __init__(self, id: int, collection: (list[(Plant, Animal)])) -> None:
        self.__id: int = id
        self.collection: list[(Plant, Animal)] = collection

    @property
    def id(self) -> int:
        return self.__id

    def to_json(self):
        with open("state.json", "rw"):
            json.dumps(self.__dir__())


