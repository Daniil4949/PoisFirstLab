import random
from plants.plant import Plant
from animals.abstract_classes import Herbivorous


class Roe(Herbivorous):
    def __init__(self, size: int = 5, saturation: int = 5,
                 gender: str = "male", age: int = 0):
        self.__size: int = size
        self.__saturation: int = saturation
        self.__gender: str = gender
        self.__age: int = age

    @property
    def age(self) -> int:
        return self.__age

    @property
    def size(self) -> int:
        return self.__size

    @property
    def saturation(self) -> int:
        return self.__saturation

    @property
    def gender(self) -> str:
        return self.__gender

    def multipy(self, other):
        if isinstance(other, Roe):
            if other.gender != self.gender:
                return Roe(size=int((self.size + other.size) / 2),
                           saturation=int((self.saturation + other.saturation) / 2),
                           gender=random.choices(['male', 'female'])
                           )
            else:
                print("Different genders are needed for multipy")
        else:
            print("The same type is needed for multipy")

    def move(self):
        print("Roe is running")

    def eat(self, meal):
        if isinstance(meal, Plant):
            self.__saturation += meal.value
            meal.die()
        else:
            print("Only plants can be eaten by roe")

    def get_old(self) -> None:
        self.__age += 1
        self.die()

    def get_hungry(self) -> None:
        self.__saturation -= 1
        self.die()

    def __del__(self) -> None:
        del self

    def die(self) -> None:
        if self.__age >= 10:
            del self
        elif self.__saturation <= 0:
            del self

    def __str__(self) -> str:
        return f"Class: Roe " \
               f"Saturation: {self.__saturation} " \
               f"Size: {self.__size} " \
               f"Age: {self.__age} "
