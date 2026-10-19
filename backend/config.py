from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):

    SQLITE_DB_FILE: str


    @property
    def db_url_sqlite(self):
        return f"sqlite+aiosqlite:///{self.SQLITE_DB_FILE}.db"

    model_config = SettingsConfigDict(env_file=".env")
settings = Settings()