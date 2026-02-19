# 🎮 CRUD de Inventario de Videojuegos con Python

Este proyecto consiste en un CRUD que permite consultar, registrar, actualizar y eliminar videojuegos en el inventario del usuario.

## 🚀 Tecnologías usadas

- Python  
- MySQL  
- PyCharm  

## 📦 Instalación y uso

1. **Clonar o descargar** este repositorio en tu PC.

2. **Abrir el proyecto en PyCharm** (recomendado).

3. **Crear la base de datos** antes de ejecutar el proyecto:
   - Crear una base de datos en MySQL.
   - Crear una tabla llamada `juegos` con la siguiente instrucción:
   ```sql
   CREATE TABLE juegos (
       id INT NOT NULL AUTO_INCREMENT,
       nombre VARCHAR(100) NOT NULL,
       voces VARCHAR(20) DEFAULT NULL,
       textos VARCHAR(20) DEFAULT NULL,
       consola VARCHAR(20) DEFAULT NULL,
       formato VARCHAR(20) DEFAULT NULL,
       comentarios VARCHAR(200) DEFAULT NULL,
       PRIMARY KEY (id)
   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
   ```

4. En el archivo `conexion.py`, configurar las variables de conexión a la base de datos:
   - host  
   - port  
   - user  
   - password  
   - database  

5. Ejecutar el proyecto desde el archivo `main.py` o, desde la terminal, ubicarse en la carpeta del proyecto y ejecutar:
   ```bash
   python main.py
   ```

## 👨‍💻 Autor
Daniel Gaviria

