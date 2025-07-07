from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  

class Settings(BaseSettings):
    # PostgreSQL
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str

    # AWS Redshift
    redshift_user: str
    redshift_password: str
    redshift_host: str
    redshift_port: int
    redshift_db: str

    # AWS S3
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str
    s3_bucket_name: str

    # AWS Glue
    glue_catalog_id: str
    glue_database_name: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()