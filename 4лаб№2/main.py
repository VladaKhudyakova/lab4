class Animal:
    pass


class Dog:
    pass


if "_main_" == _name_:
    animal = Animal("Барсик", 3, "Кошка")
    print(animal)
    print(repr(animal))
    print(animal.make_sound())

    dog = Dog("Рекс", 5, "Немецкая овчарка", ["сидеть", "лежать"])
    print(dog)
    print(repr(dog))
    print(dog.make_sound())
    dog.add_trick("голос")
    print(dog.perform_tricks())



class Animal:
    """
    Базовый класс для представления животных.

    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного.
        species (str): Вид животного.
    """

    def _init_(self, name: str, age: int, species: str) -> None:
        """
        Конструктор базового класса Animal.

        Аргументы:
            name (str): Имя животного.
            age (int): Возраст животного.
            species (str): Вид животного.
        """
        self.name = name
        self.age = age
        self.species = species

    def _str_(self) -> str:
        """
        Возвращает строковое представление объекта.

        Возвращает:
            str: Строка с информацией о животном.
        """
        return f"{self.name} ({self.species}), возраст: {self.age} лет"

    def _repr_(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        Возвращает:
            str: Формальное строковое представление.
        """
        return f"Animal(name={self.name}, age={self.age}, species={self.species})"

    def make_sound(self) -> str:
        """
        Возвращает звук, который издает животное.

        Возвращает:
            str: Звук животного.
        """
        return "Неизвестный звук"


class Dog(Animal):
    """
    Дочерний класс для представления собак.

    Атрибуты:
        name (str): Имя собаки.
        age (int): Возраст собаки.
        breed (str): Порода собаки.
        tricks (List[str]): Список команд, которые знает собака.
    """

    def _init_(self, name: str, age: int, breed: str, tricks: List[str] = None) -> None:
        """
        Конструктор дочернего класса Dog.

        Аргументы:
            name (str): Имя собаки.
            age (int): Возраст собаки.
            breed (str): Порода собаки.
            tricks (List[str]): Список команд, которые знает собака.
        """
        super()._init_(name, age, species="Собака")
        self.breed = breed
        self.tricks = tricks if tricks is not None else []

    def _str_(self) -> str:
        """
        Возвращает строковое представление объекта.

        Возвращает:
            str: Строка с информацией о собаке.
        """
        return f"{self.name} ({self.breed}), возраст: {self.age} лет, знает команд: {len(self.tricks)}"

    def _repr_(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        Возвращает:
            str: Формальное строковое представление.
        """
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed}, tricks={self.tricks})"

    def make_sound(self) -> str:
        """
        Возвращает звук, который издает собака.

        Возвращает:
            str: Звук собаки.
        """
        return "Гав-гав!"

    def add_trick(self, trick: str) -> None:
        """
        Добавляет новую команду в список команд собаки.

        Аргументы:
            trick (str): Новая команда.
        """
        self.tricks.append(trick)

    def perform_tricks(self) -> str:
        """
        Возвращает строку с командами, которые выполняет собака.

        Возвращает:
            str: Строка с командами.
        """
        if not self.tricks:
            return f"{self.name} не знает ни одной команды."
        return f"{self.name} выполняет команды: {', '.join(self.tricks)}"


