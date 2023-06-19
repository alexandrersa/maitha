from pydantic import BaseSettings
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Settings(BaseSettings):
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str


def get_connection():
    settings = Settings()

    return create_engine(
        "postgresql://{0}:{1}@{2}:{3}/{4}".format(
            settings.DATABASE_USER,
            settings.DATABASE_PASSWORD,
            settings.DATABASE_HOST,
            settings.DATABASE_PORT,
            settings.DATABASE_NAME,
        ),
    )


engine = get_connection()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)
