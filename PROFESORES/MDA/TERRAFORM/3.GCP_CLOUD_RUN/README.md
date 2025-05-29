# Ejercicio de GCP Cloud Run

Elabora este proyecto de terraform para crear un servicio de Cloud Run en GCP, con las siguientes características:

## Requisitos

- Crear un servicio de Cloud Run
- Desplegar esta imagen de docker:
  - https://hub.docker.com/r/shahdev007/hangman
- Exponer el servicio en la URL: `https://hangman-<ID_DE_PROYECTO>.<region>.run.app/`
- Debe ser un servicio público y sin autenticación
- Solo debe tener una instancia y no escalar
- El servicio debe tener un límite de 1 GB de memoria y 1 vCPU
- El servicio debe tener un límite de 1000 peticiones concurrentes
