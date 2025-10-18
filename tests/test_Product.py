from src.Product import Product


def test_product_init(product: Product) -> None:
    """Проверка инициализации класса Product."""

    assert product.name == "onion"
    assert product.description == "for a salad"
    assert product.price == 5.55
    assert product.quantity == 2
