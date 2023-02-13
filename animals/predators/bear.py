import random
from animals.abstract_classes import Herbivorous
from animals.abstract_classes import Predator


class Bear(Predator):

    def __init__(self, size: int = 10, strength: int = 10, saturation: int = 9,
                 gender: str = "male", age: int = 0):
        self.__size: int = size
        self.__strength: int = strength
        self.__saturation: int = saturation
        self.__gender: str = gender
        self.__age: int = age

    def multipy(self, other):
        if isinstance(other, Bear):
            if other.gender != self.gender:
                return Bear(size=int((self.size + other.size) / 2),
                            saturation=int((self.saturation + other.saturation) / 2),
                            strength=int((self.strength + other.strength) / 2),
                            gender=random.choices(['male', 'female'])
                            )
            else:
                print("Different genders are needed")
        else:
            print("The same type is needed")

    def move(self):
        print("Bear is hunting")

    def eat(self, meal: (Predator, Herbivorous)):
        if not isinstance(meal, Bear):
            if isinstance(meal, Herbivorous):
                self.__saturation += meal.size
            elif isinstance(meal, Predator):
                if self.__strength >= meal.strength:
                    self.__saturation += meal.size
                else:
                    del self
        else:
            print("Cannibalism does not exist in this game")

    def get_old(self):
        self.__age += 1

    def get_hungry(self):
        self.__saturation -= 1

    def die(self):
        del self

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

    @property
    def strength(self) -> int:
        return self.__strength

    def __del__(self):
        del self

    def __str__(self) -> str:
        return f"Class: Bear " \
               f"Saturation: {self.__saturation} " \
               f"Strength: {self.__strength} " \
               f"Size: {self.__size} " \
               f"Age: {self.__age} "
