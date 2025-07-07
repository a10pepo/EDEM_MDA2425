import polars as pl
import pyarrow.parquet as pq
from pyiceberg.catalog import load_catalog
from pyiceberg.schema import Schema
from pyiceberg.types import (NestedField, StringType, IntegerType, FloatType, DateType, TimestampType, BooleanType)

from src.config.settings import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)


def get_iceberg_catalog():
    return load_catalog(
        "glue_catalog",
        **{
            "type": "glue",
            "region": settings.aws_region,
            "s3.endpoint": f"https://s3.{settings.aws_region}.amazonaws.com",
            "warehouse": f"s3://{settings.s3_bucket_name}"
        }
    )

def polars_to_iceberg_schema(df_schema: dict) -> Schema:
    type_mapping = {
        pl.Int64: IntegerType(),
        pl.Int32: IntegerType(),
        pl.Float64: FloatType(),
        pl.Float32: FloatType(),
        pl.String: StringType(),
        pl.Date: DateType(),
        pl.Datetime: TimestampType(),
        pl.Boolean: BooleanType()
    }
    fields = []
    for i, (name, dtype) in enumerate(df_schema.items()):
        iceberg_type = type_mapping.get(dtype, StringType())
        fields.append(NestedField(field_id=i + 1, name=name, field_type=iceberg_type, required=False))
    return Schema(*fields)

def create_iceberg_tables_from_s3():
    catalog = get_iceberg_catalog()
    tables_to_process = ['airplanes', 'passengers', 'flights', 'flight_passengers']

    for table_name in tables_to_process:
        logger.info(f"--- Procesando tabla para Iceberg: {table_name} ---")
        s3_path = f"s3://{settings.s3_bucket_name}/parquet/{table_name}/{table_name}.parquet"
        
        try:
            df = pl.read_parquet(s3_path, use_pyarrow=True)
            if df.is_empty():
                logger.warning(f"El archivo Parquet para {table_name} está vacío. Saltando.")
                continue

            full_table_name = f"{settings.glue_database_name}.{table_name}"
            iceberg_schema = polars_to_iceberg_schema(df.schema)

            try:
                table = catalog.load_table(full_table_name)
                logger.info(f"Tabla {full_table_name} ya existe. Se añadirán los datos.")
            except Exception:
                logger.info(f"Tabla {full_table_name} no encontrada. Creando nueva tabla.")
                table = catalog.create_table(full_table_name, schema=iceberg_schema)

            logger.info(f"Añadiendo {len(df)} filas a la tabla {full_table_name}.")
            table.append(df)
            logger.info(f"Datos añadidos exitosamente a {full_table_name}.")

        except Exception as e:
            logger.error(f"Error procesando la tabla {table_name}: {e}")


def main():
    logger.info("Iniciando el proceso de carga a Iceberg con PyIceberg y Polars.")
    create_iceberg_tables_from_s3()
    logger.info("Proceso de carga a Iceberg completado.")

if __name__ == "__main__":
    main()