from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from pathlib import Path
from functools import lru_cache

class AppSettings(BaseSettings):

    model_config = SettingsConfigDict(
        env_prefix="MCP_MYGUIDES_",
        env_file=None  # ← disables automatic .env reading
    )

    APP_NAME: str = "MCP MyGuides"
    APP_INSTRUCTIONS: str = "You are a helpful assistant that provides information from guides."
    GUIDES_YAML_FILENAME: str = "guides.yaml"
    GUIDES_BASE_PATH: Path = Field(default_factory=lambda: Path(__file__).parent.parent / "guides")

    @property
    def guides_yaml_path(self) -> Path:
        return self.GUIDES_BASE_PATH / self.GUIDES_YAML_FILENAME

@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()
