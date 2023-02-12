import random
from animals.predators.predator_class import Predator
from animals.herbivores.herbivores import Herbivorous


class Wolf(Predator):

    def __init__(self, size: int = 5, strength: int = 7, saturation: int = 4,
                 gender: str = "male", age: int = 0):
        # super().__init__(size=size, strength=strength, saturation=saturation, gender=gender)
        self.__size: int = size
        self.__strength: int = strength
        self.__saturation: int = saturation
        self.__gender: str = gender
        self.__age: int = age

    def multipy(self, other):
        if isinstance(other, Wolf):
            if other.gender != self.gender:
                return Wolf(size=int((self.size + other.size) / 2),
                            saturation=int((self.saturation + other.saturation) / 2),
                            strength=int((self.strength + other.strength) / 2),
                            gender=random.choices(['male', 'female'])
                            )
            else:
                print("Different genders are needed")
        else:
            print("The same type is needed")

    def move(self):
        print("Bear is moving")

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

    def eat(self, meal):
        if not isinstance(meal, Wolf):
            if isinstance(meal, Herbivorous):
                self.__saturation += meal.size
            elif isinstance(meal, Predator):
                if self.__strength >= meal.strength:
                    self.__saturation += meal.size
                    del meal
                else:
                    del self
        else:
            print("Cannibalism does not exist in this game")

    def get_old(self):
        self.__age += 1
        self.die()

    def get_hungry(self):
        self.__saturation -= 2
        self.die()

    def die(self):
        if self.saturation <= 0 or self.age >= 20:
            del self

    def __str__(self) -> str:
        return f"Class: Wolf " \
               f"Saturation: {self.__saturation} " \
               f"Strength: {self.__strength} " \
               f"Size: {self.__size} " \
               f"Age: {self.__age} "
