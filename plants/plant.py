class Plant:
    def __init__(self, name: str = "flower", value: int = 1, age: int = 0) -> None:
        self.__name: str = name
        self.__value: int = value
        self.__age: int = age

    @property
    def name(self) -> str:
        return self.__name

    @property
    def value(self) -> int:
        return self.__value

    @property
    def age(self) -> int:
        return self.__age

    def get_old(self):
        self.__age += 1

    def die(self):
        if self.__age >= 3:
            print(f'{self.__name} died')
            del self

    def get_eaten(self):
        del self

    def __delete__(self):
        del self

    def __str__(self) -> str:
        return f"Plant: {self.__name}" \
               f" Value: {self.__value}"
