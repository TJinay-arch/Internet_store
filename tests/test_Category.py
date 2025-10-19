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
