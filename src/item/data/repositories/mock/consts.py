from src.category.domain.consts import CategoriesKeys


MOCK_PHONE_DATA = dict(
    id="66823fe056bd9d750dd27202",
    name="pixel 6a",
    price=39999,
    description="Lorem ipsum",
    camera=48,
    category=dict(
        name="Телефоны",
        key=CategoriesKeys.PHONE.value,
    ),
)

MOCK_LAPTOP_DATA = dict(
    id="668a6026625155cae7473dbe",
    name="thinkpad V",
    price=99999,
    description="Lorem ipsum",
    ram=24,
    category=dict(
        name="Ноутбуки",
        key=CategoriesKeys.LAPTOP.value,
    ),
)
