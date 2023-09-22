from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerConfig(BaseModel):
    address: str
    port: str


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter='__')

    server: ServerConfig


def gather_config() -> Config:
    # TODO: Log validation error
    return Config()
