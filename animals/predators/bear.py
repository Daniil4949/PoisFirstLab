import random
from predator import Predator
from animals.herbivores.herbivores import Herbivorous


class Bear(Predator):

    def __init__(self, size: int = 10, strength: int = 10, saturation: int = 9, gender: str = "male"):
        super().__init__(size=size, strength=strength, saturation=saturation, gender=gender)
        self.__age: int = 0

    def multipy(self, other):
        if isinstance(other, Bear):
            if other.gender != self.gender:
                return Bear(size=int((self.size + other.size) / 2),
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

    def eat(self, meal: (Predator, Herbivorous)):
        if not isinstance(meal, Bear):
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

    def get_hungry(self):
        self.__saturation -= 1

    def die(self):
        if self.saturation <= 0 or self.age >= 30:
            del self

    def __str__(self) -> str:
        return f"Class: Bear " \
               f"Saturation: {self.saturation}" \
               f"Strength: {self.strength}" \
               f"Size: {self.size}" \
               f"Age: {self.age}"