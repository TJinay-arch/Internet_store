import pytest

from src.Category import Category
from src.Product import LawnGrass, Product, Smartphone


def test_category_init(category: Category, product: Product) -> None:
    """Проверка инициализации класса Category и подсчета количества категорий и продуктов."""

    assert category.name == "vegetables"
    assert category.description == "for a tasty salad"
    assert len(category.products.strip().split(",")[0:3]) == 3

    assert category.category_count == 1
    assert category.product_count == 3

    category.add_product(product)
    assert category.product_count == 4

    assert category.products == (
        "onion, 5.55 руб. Остаток: 2 шт.\n"
        "onion, 5.55 руб. Остаток: 2 шт.\n"
        "onion, 5.55 руб. Остаток: 2 шт.\n"
        "onion, 5.55 руб. Остаток: 2 шт.\n"
    )

    invalid_obj = "Некорректный объект"
    with pytest.raises(TypeError):
        category.add_product(invalid_obj)


def test_category(capsys):
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1)

    captured_print = capsys.readouterr()

    assert captured_print.out.strip() == "Смартфоны, количество продуктов: 27 шт."


def test_category_subclass(capsys):
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)
    captured_output_1 = capsys.readouterr()
    assert captured_output_1.out.strip() == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )

    with pytest.raises(TypeError):
        category_smartphones.add_product("Not a product")
