from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def multipy(self, other):
        pass

    @abstractmethod
    def die(self):
        pass

    @abstractmethod
    def eat(self, meal):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def get_old(self):
        pass

    @abstractmethod
    def get_hungry(self):
        pass


class Herbivorous(Animal):
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


class Predator(Animal):
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
