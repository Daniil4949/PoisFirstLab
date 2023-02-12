from herbivores import Herbivorous
import random
from plants.plant import Plant


class Rabbit(Herbivorous):

    def __init__(self, size: int = 3, saturation: int = 3, gender: str = "male"):
        super().__init__(size=size, strength=None, saturation=saturation, gender=gender)
        self.__age: int = 0

    def multipy(self, other):
        if isinstance(other, Rabbit):
            if other.gender != self.gender:
                return Rabbit(size=int((self.size + other.size) / 2),
                              saturation=int((self.saturation + other.saturation) / 2),
                              gender=random.choices(['male', 'female'])
                              )
            else:
                raise Exception("Different genders are needed")
        else:
            raise Exception("The same type is needed")

    def move(self):
        pass

    def eat(self, meal):
        if isinstance(meal, Plant):
            self.__saturation += meal.value
        else:
            raise Exception("Only plants can be eaten")

    def get_old(self):
        self.__age += 1
        self.__die()

    def get_hungry(self):
        self.__saturation -= 2
        self.__die()

    def __die(self):
        if self.saturation <= 0 or self.age >= 5:
            del self

    def __str__(self) -> str:
        return f"Class: Wolf " \
               f"Saturation: {self.saturation}" \
               f"Size: {self.size}" \
               f"Age: {self.age}"
