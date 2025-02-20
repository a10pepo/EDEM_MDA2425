# Evaluation Exercise - Create your first API using swagger
Imagine that you work into industry compony where there is a robot. 
We have a sensor that is monitoring the temperature of robot via real-time. The measurement is saving into a database.
Info from sensor;
- id del sensor - string
- fechamuestreo - string
- unidad - string
- medicion - number

Our api needs create the next methods;
> /getLastMeassureBySensor/{sensor}:
sensor -> string

When the methods is successful then this should return;
Measure
- code (id del sensor) - string
- fechamuestreo - string
- unidad - string
- medicion - number

When the method is not successful then  this should return;
404 -> Invalid ID supplied
400 -> Sensor not found

Steps:
- Create your yaml
- Check the format into https://editor.swagger.io/

