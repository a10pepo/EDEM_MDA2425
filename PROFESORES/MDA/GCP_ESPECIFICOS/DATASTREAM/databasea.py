import os
from google.cloud.sql.connector import Connector, IPTypes
import pymysql
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.engine.base import Engine
from datetime import datetime
import time
from faker import Faker
fake = Faker()

# Replace these variables with your own values
DB_USER = 'root'
DB_PASSWORD = '0123456789'
DB_NAME = 'animals'
DB_INSTANCE_NAME = "edem-363212:europe-southwest1:database-a"



def connect_with_connector() -> Engine:
    """
    Initializes a connection pool for a Cloud SQL instance of MySQL.

    Uses the Cloud SQL Python Connector package.
    """
    instance_connection_name = DB_INSTANCE_NAME  # e.g. 'project:region:instance'
    db_user = DB_USER  # e.g. 'my-db-user'
    db_pass = DB_PASSWORD
    db_name = DB_NAME  # e.g. 'my-database'

    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    # Initialize the Cloud SQL Python Connector
    connector = Connector()

    def getconn() -> pymysql.connections.Connection:
        conn = connector.connect(
            instance_connection_name,
            "pymysql",
            user=db_user,
            password=db_pass,
            db=db_name,
            ip_type=ip_type,
        )
        return conn

    # Create SQLAlchemy connection pool
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )
    return pool

def create_animals_table(engine: Engine):
    """
    Creates the 'animals' table if it does not exist.
    """
    metadata = MetaData()
    animals = Table(
        'animals', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('animal', String(50), nullable=False),
        Column('insert_timestamp', DateTime, default=datetime.utcnow)
    )
    metadata.create_all(engine)

def insert_random_animal(engine: Engine):
    """
    Inserts a random animal into the 'animals' table every minute.
    """
    metadata = MetaData()
    animals = Table('animals', metadata, autoload_with=engine)
    animal_list = ['Cat', 'Dog', 'Elephant', 'Giraffe', 'Lion', 'Tiger', 'Zebra', 'Monkey', 'Bear', 'Wolf']
    while True:
        with engine.connect() as connection:
            insert_stmt = animals.insert().values(
                animal=fake.random_element(elements=animal_list),
                insert_timestamp=datetime.utcnow()
            )
            connection.execute(insert_stmt)
            print(f"Inserted a new animal: {insert_stmt}")
        time.sleep(60)

# Example usage
if __name__ == "__main__":
    engine = connect_with_connector()
    create_animals_table(engine)
    insert_random_animal(engine)