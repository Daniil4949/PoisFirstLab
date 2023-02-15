import random
from plants.plant import Plant
from animals.abstract_classes import Herbivorous


class Rabbit(Herbivorous):

    def __init__(self, size: int = 3, saturation: int = 10,
                 gender: str = "male", age: int = 0):
        self.__size: int = size
        self.__saturation: int = saturation
        self.__gender: str = gender
        self.__age: int = age

    def multipy(self, other):
        """
        :param other: Rabbit
        :return: (Rabbit, None)
        Works only with rabbit with another gender
        """
        if isinstance(other, Rabbit):
            if other.gender != self.gender:
                return Rabbit(size=int((self.size + other.size) / 2),
                              saturation=int((self.saturation + other.saturation) / 2),
                              gender=random.choices(['male', 'female'])
                              )
            else:
                print("Different genders are needed for multipy")
        else:
            print("The same type is needed for multipy")

    @property
    def size(self) -> int:
        return self.__size

    @property
    def saturation(self) -> int:
        return self.__saturation

    @property
    def age(self) -> int:
        return self.__age

    @property
    def gender(self) -> str:
        return self.__gender

    def move(self) -> None:
        print("Moving in the field")

    def __del__(self) -> None:
        del self

    def __delete__(self) -> None:
        del self

    def die(self) -> None:
        if self.__age >= 5:
            del self
        elif self.__saturation <= 0:
            del self

    def eat(self, meal) -> None:
        """
        :param meal: Plant
        :return: None
        Rabbit can eat plants only
        """
        if isinstance(meal, Plant):
            self.__saturation += meal.value
            meal.die()
        else:
            print("Only plants can be eaten by rabbit")

    def get_old(self) -> None:
        self.__age += 1
        self.die()

    def get_hungry(self) -> None:
        self.__saturation -= 1
        self.die()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self) -> str:
        return f"Class: Wolf " \
               f"Saturation: {self.__saturation} " \
               f"Size: {self.__size} " \
               f"Age: {self.__age} "
