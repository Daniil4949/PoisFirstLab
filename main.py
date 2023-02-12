from animals.predators.fox import Fox
from animals.predators.bear import Bear
from animals.predators.wolf import Wolf
from plants.plant import Plant
from animals.herbivores.roe import Roe
from animals.herbivores.rabbit import Rabbit
from fields.field import Field


def main():
    for i in range(1, 5):
        field = Field(i, collection=[Plant, Plant, Plant, Plant, Bear, Wolf,
                                     Fox, Rabbit, Rabbit, Roe, Roe])
        field.to_json()


if __name__ == "__main__":
    main()
