from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    MONGO_URI: str = Field(
        "localhost:27017", env=["MONGO_URI"]
    )


class UseMockSettings(BaseSettings):
    USE_MOCK_ITEM_REPO: bool = Field(env=["USE_MOCK_ITEM_REPO"])
    USE_MOCK_PHONE_REPO: bool = Field(env=["USE_MOCK_PHONE_REPO"])
    USE_MOCK_LAPTOP_REPO: bool = Field(env=["USE_MOCK_LAPTOP_REPO"])


settings = Settings()
use_mock_settings = UseMockSettings()