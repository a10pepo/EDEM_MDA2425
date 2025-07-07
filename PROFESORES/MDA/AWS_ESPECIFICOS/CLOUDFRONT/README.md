Collecting workspace information# Ejercicio: Servir Página Web desde S3 con CloudFront usando Terraform

## Descripción

En este ejercicio, deberás crear una infraestructura en AWS que permita servir una página web estática alojada en un bucket S3 y distribuida a través de CloudFront. Toda la infraestructura debe ser creada utilizando Terraform.

## Objetivos

- Crear un bucket S3 para alojar una página web estática
- Configurar un CloudFront para distribuir el contenido del bucket S3
- Hacer que la página web sea accesible públicamente a través de CloudFront

## Requisitos previos

- Una cuenta de AWS
- AWS CLI configurado en tu máquina local
- Terraform instalado en tu máquina local
- Conocimientos básicos de AWS S3 y CloudFront
- Conocimientos básicos de Terraform

## Pasos a seguir en la consola de AWS (para referencia)

### 1. Configuración inicial

1. Inicia sesión en la consola de AWS
2. Verifica que tienes los permisos necesarios para crear recursos S3 y CloudFront

### 2. Creación del bucket S3

1. Ve a la sección S3 de la consola de AWS
2. Crea un nuevo bucket con un nombre único
3. Configura el bucket para alojamiento de sitios web estáticos
4. Establece los permisos adecuados para permitir acceso público al contenido
5. Sube un archivo HTML de prueba (index.html)

### 3. Creación de la distribución CloudFront

1. Ve a la sección CloudFront de la consola de AWS
2. Crea una nueva distribución
3. Selecciona el bucket S3 como origen
4. Configura el comportamiento de caché según tus necesidades
5. Establece el documento raíz (index.html)
6. Configura los ajustes de seguridad adecuados
7. Espera a que la distribución se despliegue (puede tardar unos minutos)

### 4. Verificación del despliegue

1. Accede a la URL de CloudFront proporcionada para verificar que tu página web se muestra correctamente

## Entregable

Deberás entregar un proyecto de Terraform que incluya:

1. Archivos de configuración de Terraform (.tf) que creen la infraestructura
2. Un archivo README.md con:
   - Instrucciones para ejecutar el código
   - Explicación de la arquitectura creada
   - Capturas de pantalla que demuestren el funcionamiento

## Consideraciones adicionales

- Asegúrate de que tu código de Terraform sigue las mejores prácticas
- Utiliza variables para configurar parámetros como el nombre del bucket
- Implementa medidas de seguridad adecuadas
- Considera la posibilidad de usar módulos de Terraform para mejorar la reutilización del código

## Recursos útiles

- [Documentación de Terraform para AWS S3](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket)
- [Documentación de Terraform para AWS CloudFront](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudfront_distribution)
