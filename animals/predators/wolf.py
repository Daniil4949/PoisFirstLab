import random
from predator import Predator
from animals.herbivores.herbivores import Herbivorous


class Wolf(Predator):

    def __init__(self, size: int = 5, strength: int = 7, saturation: int = 4, gender: str = "male"):
        super().__init__(size=size, strength=strength, saturation=saturation, gender=gender)
        self.__age: int = 0

    def multipy(self, other):
        if isinstance(other, Wolf):
            if other.gender != self.gender:
                return Wolf(size=int((self.size + other.size) / 2),
                            saturation=int((self.saturation + other.saturation) / 2),
                            strength=int((self.strength + other.strength) / 2),
                            gender=random.choices(['male', 'female'])
                            )
            else:
                raise Exception("Different genders are needed")
        else:
            raise Exception("The same type is needed")

    def move(self):
        pass

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
            raise Exception("Cannibalism does not exist in this game")

    def get_old(self):
        self.__age += 1
        self.__die()

    def get_hungry(self):
        self.__saturation -= 2
        self.__die()

    def __die(self):
        if self.saturation <= 0 or self.age >= 20:
            del self

    def __str__(self) -> str:
        return f"Class: Wolf " \
               f"Saturation: {self.saturation}" \
               f"Strength: {self.strength}" \
               f"Size: {self.size}" \
               f"Age: {self.age}"
