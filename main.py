import json
from animals.predators.fox import Fox
from animals.predators.bear import Bear
from animals.predators.wolf import Wolf
from plants.plant import Plant
from animals.herbivores.roe import Roe
from animals.herbivores.rabbit import Rabbit
from fields.field import Field
from print_fields import manipulate_fields

collection = [Plant(), Plant(), Plant(), Plant(),
              Rabbit(gender="female"), Rabbit(gender="male"), Roe(gender="male"),
              Roe(gender="female"), Bear(gender="male"), Fox(gender="female"),
              Wolf(gender="male")]


def to_json(data: list[Field]) -> dict:
    info = dict()
    for i in range(len(data)):
        item = {i + 1: {
            "collection": [x.__dict__ for x in data[i].collection]}}
        info = info | item
    return info


def from_json():
    objects = []
    with open("state.json", "r") as file:
        result = file.read()
        info = json.loads(result)
    for item in list(info.items()):
        for element in list(item[1].values()):
            field = Field(id=item[0], collection=[])
            for i in range(len(element)):
                if "Fox" in list(element[i].keys())[0]:
                    field.collection.append(Fox(*list(element[i].values())))
                if "Wolf" in list(element[i].keys())[0]:
                    field.collection.append(Wolf(*list(element[i].values())))
                if "Bear" in list(element[i].keys())[0]:
                    field.collection.append(Bear(*list(element[i].values())))
                if "Rabbit" in list(element[i].keys())[0]:
                    field.collection.append(Rabbit(*list(element[i].values())))
                if "Roe" in list(element[i].keys())[0]:
                    field.collection.append(Roe(*list(element[i].values())))
                if "Plant" in list(element[i].keys())[0]:
                    field.collection.append(Plant(*list(element[i].values())))
            objects.append(field)
    return objects


def create_collection():
    result = []
    for i in range(1, 5):
        field = Field(i, collection=collection)
        result.append(field)
    info = to_json(result)
    with open("state.json", "w") as file:
        file.write(json.dumps(info))


def main():
    # create_collection()
    lst = from_json()
    try:
        while True:
            manipulate_fields(lst)
    except KeyboardInterrupt:
        dict_data = to_json(lst)
        with open("state.json", "w") as file:
            file.write(json.dumps(dict_data))
        print('\nBy!\n')


if __name__ == "__main__":
    main()
