from sqlalchemy import create_engine
from src.config.settings import settings
from src.db.models import Base
from src.utils.logger import get_logger

logger = get_logger(__name__)

def create_database_tables():
    try:
        logger.info("Conectando a la base de datos para crear las tablas...")
        db_url = f"postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
        engine = create_engine(db_url)
        
        logger.info("Creando todas las tablas definidas en los modelos de SQLAlchemy...")
        Base.metadata.create_all(engine)
        
        logger.info("Tablas creadas exitosamente.")
    except Exception as e:
        logger.error(f"Error al crear las tablas: {e}")
        raise

if __name__ == "__main__":
    create_database_tables()
