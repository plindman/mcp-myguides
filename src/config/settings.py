from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from functools import lru_cache

class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    GUIDES_BASE_PATH: Path = Path("guides")
    GUIDES_YAML_FILENAME: str = "guides.yaml"
    APP_NAME: str = "MCP MyGuides"
    APP_INSTRUCTIONS: str = "You are a helpful assistant that provides information from guides."

    @property
    def guides_yaml_path(self) -> Path:
        return self.GUIDES_BASE_PATH / self.GUIDES_YAML_FILENAME

@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()
