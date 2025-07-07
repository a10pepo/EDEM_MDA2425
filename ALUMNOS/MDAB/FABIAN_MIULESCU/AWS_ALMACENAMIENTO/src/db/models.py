from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Airplane(Base):
    __tablename__ = 'airplanes'
    plateNumber = Column(String, primary_key=True)
    type = Column(String)
    lastMaintenanceDate = Column(Date)
    nextMaintenanceDate = Column(Date)
    capacity = Column(Integer)
    ownerId = Column(String)
    ownerName = Column(String)
    hangarId = Column(String)
    fuel_capacity = Column(Integer)
    flights = relationship("Flight", back_populates="airplane")

class Passenger(Base):
    __tablename__ = 'passengers'
    passengerId = Column(String, primary_key=True)
    name = Column(String)
    nationalId = Column(String, unique=True)
    dateOfBirth = Column(Date)
    flights = relationship("FlightPassenger", back_populates="passenger")

class Flight(Base):
    __tablename__ = 'flights'
    flightId = Column(String, primary_key=True)
    plateNumber = Column(String, ForeignKey('airplanes.plateNumber'))
    arrivalTime = Column(DateTime)
    departureTime = Column(DateTime)
    fuelConsumption = Column(Float)
    occupiedSeats = Column(Integer)
    origin = Column(String)
    destination = Column(String)
    airplane = relationship("Airplane", back_populates="flights")
    passengers = relationship("FlightPassenger", back_populates="flight")

class FlightPassenger(Base):
    __tablename__ = 'flight_passengers'
    flightId = Column(String, ForeignKey('flights.flightId'), primary_key=True)
    passengerId = Column(String, ForeignKey('passengers.passengerId'), primary_key=True)
    status = Column(String) 
    flight = relationship("Flight", back_populates="passengers")
    passenger = relationship("Passenger", back_populates="flights")
