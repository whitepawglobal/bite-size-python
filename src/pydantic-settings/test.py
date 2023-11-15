from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class BaseDatabaseConfig(BaseSettings):

    #'<YOUR_DB_USER_NAME>'
    DB_USER : str

    #'<YOUR_DB_PASSWORD>'
    DB_PASSWORD : str

    #'<YOUR_DB_NAME>'
    DB_NAME : str

    model_config = SettingsConfigDict(env_file="config", case_sensitive=True)


if __name__ == "__main__":


    config  = BaseDatabaseConfig()

    print(config.DB_USER)


    print(config.model_dump())
