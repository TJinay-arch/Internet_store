from src.Product import Product


def test_product_init(capsys, product: Product) -> None:
    """Проверка инициализации класса Product."""

    assert product.name == "onion"
    assert product.description == "for a salad"
    assert product.price == 5.55
    assert product.quantity == 2

    sample = {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }
    assert product.new_product(sample).name == "Samsung Galaxy C23 Ultra"

    product.price = 30
    assert product.price == 30

    product.price = -100
    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"