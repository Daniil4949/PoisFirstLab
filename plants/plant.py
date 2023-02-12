class Plant:
    def __init__(self, name: str = "flower", value: int = 1) -> None:
        self.__name: str = name
        self.__value: int = value

    @property
    def name(self) -> str:
        return self.__name

    @property
    def value(self) -> int:
        return self.__value

    def get_eaten(self):
        del self

    def __str__(self) -> str:
        return f"Plant: {self.__name}" \
               f" Value: {self.__value}"
