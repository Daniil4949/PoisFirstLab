from time import sleep
from plants.plant import Plant
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
            sleep(0.2)
            if isinstance(item, Plant):
                sleep(0.2)
                print(f"{item.name} just existing")
                item.get_old()
                item.die()
            if isinstance(item, Herbivorous):
                discover(item, element.collection)
                item.get_hungry()
                item.get_old()
                item.die()
            elif isinstance(item, Predator):
                discover(item, element.collection)
                item.get_hungry()
                item.get_old()
                item.die()


def discover(item, collection):
    for obj in collection:
        if isinstance(obj, Plant):
            sleep(0.2)
            print(f"Herbivorous is eating")
            item.eat(obj)
            collection.pop(collection.index(obj))
        if type(item) == type(obj) and obj.gender != item.gender:
            item.multipy(obj)
            print("New animal on the field")
        if isinstance(item, Predator):
            print(f"Predator is eating")
            item.eat(obj)
            obj.die()
            print("Animal died")
        if isinstance(obj, Predator):
            print(f"Predator is eating")
            obj.eat(item)
            item.die()
            print("Animal died")
        item.get_hungry()
        item.get_old()
        item.die()
