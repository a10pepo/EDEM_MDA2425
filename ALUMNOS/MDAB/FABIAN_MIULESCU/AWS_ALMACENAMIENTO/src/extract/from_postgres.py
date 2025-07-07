import polars as pl
from sqlalchemy import create_engine
from src.config.settings import settings

def get_postgres_engine():
    db_url = f"postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
    return create_engine(db_url)

def extract_from_postgres(table_name: str) -> pl.DataFrame:
    engine = get_postgres_engine()
    query = f'SELECT * FROM "{table_name}"'
    df = pl.read_database(query, engine.connect())
    return df

if __name__ == '__main__':
    airplanes_df = extract_from_postgres('airplanes')
    print("Aviones extraídos:")
    print(airplanes_df)

    flights_df = extract_from_postgres('flights')
    print("\nVuelos extraídos:")
    print(flights_df)

