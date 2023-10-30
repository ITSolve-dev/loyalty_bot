from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import HttpUrl


class ApiSettings(BaseSettings):
    BASE_HOST: HttpUrl
    VERSION_URI: str
    PROFILES_URL: HttpUrl
    USERS_URL: HttpUrl
    INSTITUTIONS_URL: HttpUrl
    SCANS_URL: HttpUrl

    model_config = SettingsConfigDict(env_prefix="API__", case_sensitive=False)
