from abc import ABC, abstractmethod

from src.MixinInfo import CreationInfoMixin


class BaseProduct(ABC):
    @abstractmethod
    def display_details(self) -> str:
        """Отображение детальной информации о продукте."""
        pass


class Product(BaseProduct, CreationInfoMixin):
    """Класс описывающий сущность продукты."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    def display_details(self) -> str:
        """Отображение детальной информации о продукте."""
        return f"{self.name}, {self.description}, {self.__price}, {self.quantity}"

    @classmethod
    def new_product(cls, product: dict):
        return cls(product["name"], product["description"], product["price"], product["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(self, Product):
            total_cost = self.__price * self.quantity + other.__price * other.quantity
            return total_cost
        else:
            raise TypeError("Добавлять можно только объекты класса Product или его наследников.")


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def display_details(self) -> str:
        """Отображение детальной информации о продукте."""
        return (
            f"{self.name}, {self.description}, {self.__price}, {self.quantity}, {self.efficiency}, {self.model},"
            f"{self.memory}, {self.color}"
        )


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def display_details(self) -> str:
        """Отображение детальной информации о продукте."""
        return (
            f"{self.name}, {self.description}, {self.__price}, {self.quantity}, {self.country},"
            f"{self.germination_period}, {self.color}"
        )
