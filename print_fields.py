import json
from fields.field import Field
from time import sleep
from animals.predators.fox import Fox
from animals.predators.bear import Bear
from animals.predators.wolf import Wolf
from plants.plant import Plant
from animals.herbivores.roe import Roe
from animals.herbivores.rabbit import Rabbit
from fields.field import Field
from animals.abstract_classes import Herbivorous
from animals.abstract_classes import Predator


def illustrate(objects: list[Field]):
    for field in objects:
        print(f"Field number - {field.id}")
        for element in field.collection:
            sleep(0.2)
            print(element)


def manipulate_fields(objects: list[Field]):
    for element in objects:
        for item in element.collection:
            if isinstance(item, Plant):
                sleep(0.2)
                print(f"{item.name} just existing")

            if isinstance(item, Herbivorous):
                discover(item, element.collection)
            elif isinstance(item, Predator):
                discover(item, element.collection)


def discover(item, collection):
    for obj in collection:
        if isinstance(obj, Plant):
            sleep(0.2)
            print(f"Herbivorous is eating")
            item.eat(obj)
        if type(item) == type(obj) and obj.gender != item.gender:
            item.multipy(obj)
            print("New animal on the field")
        if isinstance(obj, Predator):
            print(f"Predator is eating")
            obj.eat(item)
            item.die()
            print("Animal died")
            continue
        item.get_hungry()
        item.get_old()
