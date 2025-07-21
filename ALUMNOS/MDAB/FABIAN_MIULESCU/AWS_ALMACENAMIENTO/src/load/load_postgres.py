import polars as pl
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert
from src.config.settings import settings
from src.db.models import Airplane, Passenger, Flight, FlightPassenger
from initial_info import airplanes, passengers, flights

def get_db_session():
    db_url = f"postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    return Session()

def upsert(session, model, data, primary_key):
    for record in data:
        stmt = insert(model).values(**record)
        stmt = stmt.on_conflict_do_update(
            index_elements=[primary_key],
            set_={key: getattr(stmt.excluded, key) for key in record if key != primary_key}
        )
        session.execute(stmt)
    session.commit()

def load_data_to_postgres():
    session = get_db_session()

    airplanes_df = pl.DataFrame(airplanes)
    upsert(session, Airplane, airplanes_df.to_dicts(), 'plateNumber')

    passengers_df = pl.DataFrame(passengers)
    upsert(session, Passenger, passengers_df.to_dicts(), 'passengerId')

    flights_df = pl.DataFrame(flights)
    flight_passengers_data = []
    for flight in flights_df.iter_rows(named=True):
        for passenger_id, status in flight['passengerIds']:
            flight_passengers_data.append({
                'flightId': flight['flightId'],
                'passengerId': passenger_id,
                'status': status
            })
    flights_to_load = flights_df.drop('passengerIds')
    upsert(session, Flight, flights_to_load.to_dicts(), 'flightId')

    if flight_passengers_data:
        flight_passengers_df = pl.DataFrame(flight_passengers_data)
        for record in flight_passengers_df.to_dicts():
            session.query(FlightPassenger).filter_by(
                flightId=record['flightId'], 
                passengerId=record['passengerId']
            ).delete(synchronize_session=False)
            session.add(FlightPassenger(**record))
        session.commit()

    session.close()
    print("Datos cargados exitosamente en PostgreSQL.")

if __name__ == "__main__":
    load_data_to_postgres()
