from src.category.data.repositories.mock.consts import MOCK_CATEGORY_DATA
from src.category.domain.repositories.category_repo import ICategoryRepository
from src.category.domain.entities import Category


class MockCategoryRepository(ICategoryRepository):
    async def get_categories(self) -> list[Category]:
        return [
            Category(**MOCK_CATEGORY_DATA)
        ]