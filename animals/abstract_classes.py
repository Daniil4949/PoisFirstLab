from abc import ABC


class Animal(ABC):

    def multipy(self, other):
        pass

    def die(self):
        pass

    def eat(self, meal):
        pass

    def move(self):
        pass

    def get_old(self):
        pass

    def get_hungry(self):
        pass

    def get_fed(self, value: int):
        pass