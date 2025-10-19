from src.Product import Product


class Category:
    """Класс описывающий сущность категории."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию. Допускаются только объекты класса Product или его наследники.
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Добавлять можно только объекты класса Product или его наследников.")

    @property
    def products(self):
        products = ""
        for product in self.__products:
            products += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products
