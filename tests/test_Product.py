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
        "quantity": 5,
    }
    assert product.new_product(sample).name == "Samsung Galaxy C23 Ultra"

    product.price = 30
    assert product.price == 30

    product.price = -100
    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"

def test_product_magic(capsys):

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    print(product1)

    captured_print = capsys.readouterr()

    assert captured_print.out.strip() == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

def test_product_add():

    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    assert product2 + product3 == 2114000.0