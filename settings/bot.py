from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    TOKEN: str

    model_config = SettingsConfigDict(env_prefix="BOT__", case_sensitive=False)
