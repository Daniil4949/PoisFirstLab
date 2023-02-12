from animals.abstract_classes import Animal


class Predator(Animal):

    def __int__(self, size: int, strength: int, saturation: int, gender: str) -> None:
        self.__size: int = size
        self.__strength: int = strength
        self.__saturation: int = saturation
        self.__gender: str = gender
        self.__age: int = 0

    @property
    def size(self) -> int:
        return self.__size

    @property
    def strength(self) -> int:
        return self.__strength

    @property
    def saturation(self) -> int:
        return self.__saturation

    @property
    def gender(self) -> str:
        return self.__gender

    @property
    def age(self) -> int:
        return self.__age

