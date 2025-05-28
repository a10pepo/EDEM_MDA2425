# Ejercicio: Crear un Registro ECR y Subir una Imagen Docker usando Terraform

## Descripción

En este ejercicio, deberás crear un registro de Amazon Elastic Container Registry (ECR) utilizando Terraform y luego subir una imagen Docker local a dicho registro.

## Objetivos

- Crear un repositorio ECR utilizando Terraform
- Construir una imagen Docker en tu entorno local
- Autenticarte en el registro ECR
- Etiquetar y subir la imagen Docker al repositorio ECR

## Requisitos previos

- Una cuenta de AWS
- AWS CLI configurado en tu máquina local
- Terraform instalado en tu máquina local
- Docker instalado en tu máquina local
- Conocimientos básicos de AWS ECR
- Conocimientos básicos de Docker
- Conocimientos básicos de Terraform

## Pasos a seguir en la consola de AWS (para referencia)

### 1. Configuración inicial

1. Inicia sesión en la consola de AWS
2. Verifica que tienes los permisos necesarios para crear recursos ECR

### 2. Creación del repositorio ECR

1. Ve a la sección ECR de la consola de AWS
2. Crea un nuevo repositorio con un nombre descriptivo
3. Configura las opciones de escaneo de seguridad y mutabilidad de tags según tus necesidades
4. Observa la URI del repositorio (lo necesitarás para subir imágenes)

### 3. Preparación de la imagen Docker

1. Crea un Dockerfile para tu aplicación
2. Construye la imagen Docker localmente utilizando el comando `docker build`
3. Verifica que la imagen funciona correctamente ejecutándola con `docker run`

### 4. Subida de la imagen al repositorio ECR

1. Autentica el Docker CLI con ECR usando el comando AWS CLI
2. Etiqueta tu imagen local con la URI del repositorio ECR
3. Sube la imagen etiquetada a ECR con `docker push`
4. Verifica en la consola de AWS que la imagen se ha subido correctamente

### 5. Verificación del despliegue

1. Comprueba en la consola ECR que tu imagen está disponible
2. Verifica que puedes descargar la imagen desde ECR con `docker pull`

## Entregable

Deberás entregar un proyecto de Terraform que incluya:

1. Archivos de configuración de Terraform (.tf) que creen el repositorio ECR
2. Un archivo README.md con:
   - Instrucciones para ejecutar el código de Terraform
   - Comandos Docker para construir, etiquetar y subir la imagen
   - Explicación de la arquitectura creada
   - Capturas de pantalla que demuestren el funcionamiento

## Consideraciones adicionales

- Asegúrate de que tu código de Terraform sigue las mejores prácticas
- Utiliza variables para configurar parámetros como el nombre del repositorio
- Implementa políticas de ciclo de vida para gestionar las imágenes antiguas
- Considera implementar escaneo de vulnerabilidades para tus imágenes

## Recursos útiles

- [Documentación de Terraform para AWS ECR](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecr_repository)
- [Documentación de AWS sobre ECR](https://docs.aws.amazon.com/ecr/latest/userguide/what-is-ecr.html)
- [Guía de Docker para etiquetar y subir imágenes](https://docs.docker.com/engine/reference/commandline/push/)
