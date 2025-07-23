from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    GUIDES_BASE_PATH: Path = Path("guides")
    GUIDES_YAML_FILENAME: str = "guides.yaml"

    @property
    def guides_yaml_path(self) -> Path:
        return self.GUIDES_BASE_PATH / self.GUIDES_YAML_FILENAME

def get_settings() -> AppSettings:
    return AppSettings()
