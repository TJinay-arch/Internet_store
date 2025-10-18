import json
import os
from typing import Any

from src.Category import Category
from src.Product import Product


def read_json(path: str) -> dict:
    abs_path = os.path.abspath(path)
    with open(abs_path, "r", encoding="UTF-8") as file:
        data: dict = json.load(file)

    return data


def create_objects_from_json(data: Any) -> list:
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
