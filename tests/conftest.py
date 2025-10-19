import json
import os
from typing import Any, Generator

import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def product() -> Product:
    return Product("onion", "for a salad", 5.55, 2)


@pytest.fixture(scope="function")
def category() -> Category:
    return Category(
        "vegetables",
        "for a tasty salad",
        [
            Product("onion", "for a salad", 5.55, 2),
            Product("onion", "for a salad", 5.55, 2),
            Product("onion", "for a salad", 5.55, 2),
        ],
    )


@pytest.fixture(scope="session")
def sample_data() -> list:
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
            "станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


# Подготовка фикстуры пути к файлу
@pytest.fixture(scope="session")
def temp_file(tmpdir_factory: Any, sample_data: list) -> Generator[str, Any, None]:
    filename = tmpdir_factory.mktemp("data").join("sample.json")
    with open(filename, "w") as f:
        json.dump(sample_data, f)
    yield str(filename)
    os.remove(str(filename))  # Чистка временных файлов
