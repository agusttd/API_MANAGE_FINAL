from servicios.api import obtener_datos
from modelos.todos import Todo
from modelos.users import User
from negocio.procesamiento import procesar_todos
from datos.conexion import crear_tablas, insertar_users, insertar_todos, obtener_users, obtener_todos

def main():
    crear_tablas()  #Asegurarse de que las tablas existan!!!1

    while True:
        print("\nBienvenido al sistema de gestión de datos")
        print("1. Obtener y guardar usuarios de la API")
        print("2. Obtener y guardar tareas de la API")
        print("3. Consultar usuarios almacenados")
        print("4. Consultar tareas almacenadas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nObteniendo usuarios desde la API...")
            users_data = obtener_datos("users")
            users = [User(**user) for user in users_data]
            insertar_users(users)
            print(f"{len(users)} usuarios guardados en la base de datos.")

        elif opcion == "2":
            print("\nObteniendo tareas desde la API...")
            todos_data = obtener_datos("todos")
            for todo in todos_data: #se convierte el 'userId' a 'user_id' en los datos obtenidos
                todo["user_id"] = todo.pop("userId")
            todos = [Todo(**todo) for todo in todos_data] #se cream instancias de Todo con los datos corregidos

            insertar_todos(todos)
            print(f"{len(todos)} tareas guardadas en la base de datos.")


        elif opcion == "3":
            print("\nConsultando usuarios almacenados...")
            users = obtener_users()
            for user in users:
                print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")

        elif opcion == "4":
            print("\nConsultando tareas almacenadas...")
            todos = obtener_todos()
            for todo in todos:
                print(f"ID: {todo['id']}, User ID: {todo['user_id']}, Title: {todo['title']}, Completed: {todo['completed']}")

        elif opcion == "5":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
