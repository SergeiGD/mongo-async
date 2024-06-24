import decimal
from src.item.domain.entities import Phone
from src.item.domain.repositories.phone_repo import CreatePhoneRequest, IPhoneRepository


class PhoneInteractor:
    def __init__(
        self,
        phone_repo: IPhoneRepository,
    ) -> None:
        self._phone_repo = phone_repo

    async def get_phones(self) -> list[Phone]:
        return await self._phone_repo.get_phones()
    
    async def create_phone(
        self,
        name: str,
        price: decimal,
        description: str,
        camera: int,
    ) -> Phone:
        return await self._phone_repo.create_phone(
            CreatePhoneRequest(
                name=name,
                price=price,
                description=description,
                camera=camera,
            )
        )
    