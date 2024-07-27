from src.category.domain.entities import Category


def map_category(category: dict) -> Category:
    return Category(
        name=category["name"],
        key=category["key"],
    )
