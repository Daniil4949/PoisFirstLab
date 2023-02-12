from animals.abstract_classes import Animal


class Herbivorous(Animal):

    def __int__(self, size: int, strength: int, saturation: int, gender: str) -> None:
        self.__size: int = size
        self.__saturation: int = saturation
        self.__gender: str = gender
        self.__age: int = 0

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
    def age(self) -> int:
        return self.__age
