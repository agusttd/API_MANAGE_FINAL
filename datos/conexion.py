import mysql.connector

def conectar_bd():
    """Establece la cnexion a DB"""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="api_manage"
    )

def crear_tablas():
    """Crea las tablas necesarias para el proyecto si no existen"""
    conexion = conectar_bd()
    cursor = conexion.cursor()

    tablas = [
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            username VARCHAR(255),
            email VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS todos (
            id INT PRIMARY KEY,
            user_id INT,
            title VARCHAR(255),
            completed BOOLEAN,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """
    ]

    for tabla in tablas:
        cursor.execute(tabla)

    conexion.commit()
    cursor.close()
    conexion.close()

def insertar_users(users):
    """Inserta una lista de usuarios en la base de datos."""
    conexion = conectar_bd()
    cursor = conexion.cursor()

    query = """
        INSERT INTO users (id, name, username, email)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            username = VALUES(username),
            email = VALUES(email);
    """

    for user in users:
        cursor.execute(query, (user.id, user.name, user.username, user.email))

    conexion.commit()
    cursor.close()
    conexion.close()

def insertar_user_manual(user):
    """Inserta un usuario manualmente en la base de datos."""
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            query = """
                INSERT INTO users (id, name, username, email, phone, website, address, company)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                user.id, user.name, user.username, user.email, 
                user.phone, user.website, user.address, user.company
            ))
            conexion.commit()
    except Exception as e:
        print(f"Error al insertar el usuario: {e}")
    finally:
        conexion.close()


def insertar_todos(todos):
    """Inserta una lista de tareas en la base de datos"""
    conexion = conectar_bd()
    cursor = conexion.cursor()

    query = """
        INSERT INTO todos (id, user_id, title, completed)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            title = VALUES(title),
            completed = VALUES(completed);
    """

    for todo in todos:
        cursor.execute(query, (todo.id, todo.user_id, todo.title, todo.completed))

    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_users():
    """Obtiene todos los usuarios desde la bd"""
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()

    cursor.close()
    conexion.close()
    return users

def actualizar_user(user_id, field, new_value):
    """
    Actualiza un campo específico de un usuario en la base de datos.
    """
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            query = f"UPDATE users SET {field} = %s WHERE id = %s"
            cursor.execute(query, (new_value, user_id))
            conexion.commit()
            print(f"Usuario con ID {user_id} actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar el usuario: {e}")
    finally:
        conexion.close()

def eliminar_user(user_id):
    """
    Elimina un usuario de la base de datos por su ID.
    """
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            conexion.commit()
            print(f"Usuario con ID {user_id} eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el usuario: {e}")
    finally:
        conexion.close()


def obtener_todos():
    """Obtiene todas las tareas desde la bd"""
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM todos;")
    todos = cursor.fetchall()

    cursor.close()
    conexion.close()
    return todos