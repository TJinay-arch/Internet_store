import pytest

from src.Category import Category
from src.Product import Product


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

    category1 = Category("Смартфоны",
                             "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                             [product1, product2, product3])

    print(category1)

    captured_print = capsys.readouterr()

    assert captured_print.out.strip() == "Смартфоны, количество продуктов: 27 шт."
