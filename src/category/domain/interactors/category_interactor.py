

from src.category.domain.repositories.category_repo import ICategoryRepository
from src.category.domain.entities import Category


class CategoryInteractor:
    def __init__(
        self,
        category_repo: ICategoryRepository,
    ) -> None:
        self._category_repo = category_repo

    async def get_categories(self) -> list[Category]:
        return await self._category_repo.get_categories()
    