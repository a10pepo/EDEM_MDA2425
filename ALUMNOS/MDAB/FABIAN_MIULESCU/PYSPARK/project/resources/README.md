# Proyecto PySpark y MySQL: Usuarios y Pedidos

Este proyecto muestra cómo usar **PySpark** para procesar dos conjuntos de datos (`users` y `orders`) y cómo persistir los resultados en **MySQL** mediante JDBC.

---

## 📂 **Datasets**

Los archivos CSV se encuentran en la carpeta `resources/`:

- **users.csv**  
  Contiene información de usuarios registrados:
  - `user_id` (string): Identificador único de usuario  
  - `name` (string): Nombre completo  
  - `email` (string): Correo electrónico  
  - `country` (string): País de residencia  
  - `signup_date` (date): Fecha de alta

- **orders.csv**  
  Contiene información de pedidos realizados:
  - `order_id` (string): Identificador único de pedido  
  - `user_id` (string): FK hacia `users.user_id`  
  - `product_id` (string): Identificador de producto  
  - `amount` (double): Importe total del pedido  
  - `order_date` (timestamp): Fecha y hora del pedido  
  - `status` (string): Estado del pedido (`PAID`, `CANCELLED`, etc.)

---

## 🎯 **Objetivo**

1. Demostrar la integración de **PySpark** con **MySQL** para procesar y almacenar datos.  
2. Practicar distintos tipos de transformaciones y joins entre `users` y `orders`.  
3. Extraer insights como:
   - Usuarios por país  
   - Pedidos de alto valor  
   - Conteos y agragaciones por estado y ubicación

---

## 🛠️ **Transformaciones**

### 1. Carga y guardado inicial  
- Se cargan `users.csv` y `orders.csv` en DataFrames de PySpark.  
- Se persisten ambos DataFrames en MySQL usando la función genérica `save_to_mysql()`.

### 2. Filtrados básicos  
- **Usuarios en USA**: `country == "USA"`.  
- **Pedidos > 100 USD**: `amount > 100`.

### 3. Columnas derivadas  
- En `orders`, se añade columna `status_description` con valores legibles:  
  - `"Completed"` si `status == "PAID"`  
  - `"Cancelled"` si `status == "CANCELLED"`  
  - `"Pending"` para otros estados

### 4. Joins y agregaciones  
- **Inner join** entre `users` y `orders` sobre `user_id`.  
- **Agrupación por país** para contar el número de pedidos por `country`.  
- **Pedidos de usuarios en España**, agrupados y contados por `status`.

---


