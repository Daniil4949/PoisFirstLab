from animals.herbivores.herbivores import Herbivorous
import random
from plants.plant import Plant


class Rabbit(Herbivorous):

    def __init__(self, size: int = 3, saturation: int = 3,
                 gender: str = "male", age: int = 0):
        self.__size: int = size
        self.__saturation: int = saturation
        self.__gender: str = gender
        self.__age: int = age

    def multipy(self, other):
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

    def move(self):
        print("Moving in the field")

    def eat(self, meal):
        if isinstance(meal, Plant):
            self.__saturation += meal.value
            del meal
        else:
            print("Only plants can be eaten by rabbit")

    def get_old(self):
        self.__age += 1
        self.die()

    def get_hungry(self):
        self.__saturation -= 2
        self.die()

    def die(self):
        if self.saturation <= 0 or self.age >= 5:
            del self

    def __str__(self) -> str:
        return f"Class: Wolf " \
               f"Saturation: {self.__saturation} " \
               f"Size: {self.__size} " \
               f"Age: {self.__age} "
