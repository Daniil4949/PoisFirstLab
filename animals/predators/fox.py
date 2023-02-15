from animals.abstract_classes import Predator
import random
from animals.abstract_classes import Herbivorous


class Fox(Predator):

    def __init__(self, size: int = 5, strength: int = 4, saturation: int = 4,
                 gender: str = "male", age: int = 0):
        self.__size: int = size
        self.__strength: int = strength
        self.__saturation: int = saturation
        self.__gender: str = gender
        self.__age: int = age

    def multipy(self, other):
        """
            :param other: Fox
            :return: (Fox, None)
            Works only with fox with another gender
        """
        if isinstance(other, Fox):
            if other.gender != self.gender:
                return Fox(size=int((self.size + other.size) / 2),
                           saturation=int((self.saturation + other.saturation) / 2),
                           strength=int((self.strength + other.strength) / 2),
                           gender=random.choices(['male', 'female'])
                           )
            else:
                print("Different genders are needed")
        else:
            print("The same type is needed")

    @property
    def strength(self) -> int:
        return self.__strength

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

    def __delete__(self):
        del self

    def move(self):
        print("Fox is running")

    def eat(self, meal):
        """
            :param meal: Plant
            :return: None
            Predators cannot eat each other
        """
        if not isinstance(meal, Fox):
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
        self.__age += 2
        self.die()

    def get_hungry(self):
        self.__saturation -= 2
        self.die()

    def die(self):
        if self.__age >= 5 or self.__saturation <= 0:
            del self

    def __del__(self):
        del self



    def __str__(self) -> str:
        return f"Class: Fox " \
               f"Saturation: {self.__saturation} " \
               f"Strength: {self.__strength} " \
               f"Size: {self.__size} " \
               f"Age: {self.__age} "
