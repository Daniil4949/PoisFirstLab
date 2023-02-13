from main import collection
import random
from animals.predators.fox import Fox
from animals.predators.wolf import Wolf
from animals.predators.bear import Bear
from animals.herbivores.roe import Roe
from animals.herbivores.rabbit import Rabbit
from plants.plant import Plant
from fields.field import Field
import json
from main import to_json


def add_new_item():
    result = []
    new_element = random.choices([Fox(), Wolf(), Bear(), Roe(), Rabbit(), Plant()])
    collection.append(new_element[0])
    print(f"{new_element[0]} was added!!!")
    for i in range(1, 5):
        field = Field(i, collection=collection)
        result.append(field)
    info = to_json(result)
    with open("state.json", "w") as file:
        file.write(json.dumps(info))


add_new_item()
