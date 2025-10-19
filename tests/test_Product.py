from src.Product import LawnGrass, Product, Smartphone


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


def test_product_subclass(capsys):
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    captured_out = capsys.readouterr()
    assert (
        captured_out.out.strip()
        == """Samsung Galaxy S23 Ultra
256GB, Серый цвет, 200MP камера
180000.0
5
95.5
S23 Ultra
256
Серый"""
    )

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    captured_out_2 = capsys.readouterr()
    assert (
        captured_out_2.out.strip()
        == """Газонная трава
Элитная трава для газона
500.0
20
Россия
7 дней
Зеленый"""
    )

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    captured_out_3 = capsys.readouterr()
    assert (
        captured_out_3.out.strip()
        == """2580000.0
16750.0"""
    )
