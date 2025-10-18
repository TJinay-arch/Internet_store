from src.Category import Category


def test_category_init(category: Category) -> None:
    """Проверка инициализации класса Category и подсчета количества категорий и продуктов."""

    assert category.name == "vegetables"
    assert category.description == "for a tasty salad"
    assert len(category.products) == 3

    assert category.category_count == 1
    assert category.product_count == 3
