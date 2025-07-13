-- Esquema simple para PostgreSQL
CREATE TABLE airplanes (
    plate_number VARCHAR(20) PRIMARY KEY,
    type VARCHAR(100),
    capacity INTEGER,
    owner_name VARCHAR(100)
);

CREATE TABLE passengers (
    passenger_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    national_id VARCHAR(20)
);

CREATE TABLE flights (
    flight_id VARCHAR(20) PRIMARY KEY,
    plate_number VARCHAR(20),
    origin VARCHAR(100),
    destination VARCHAR(100),
    occupied_seats INTEGER
);